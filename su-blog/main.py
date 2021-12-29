from datetime import timedelta

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt, JWTError

import database, schemas, models, crud, security


app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/api/login/oauth/access_token', status_code=status.HTTP_201_CREATED)
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = security.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={"WWW-Authenticate": "Bearer"}
        )
        
    access_token = security.create_token(
        data={'username': user.username},
        expires_delta=timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    refresh_token = security.create_token(
        data={'username': user.username},
        expires_delta=timedelta(days=security.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    
    crud.update_last_login(db, user.id)
    return {
        'token_type': 'Bearer', 
        'access_token': access_token,
        'refresh_token': refresh_token
        }


@app.post('/api/login/oauth/access_token/refresh')
async def refresh_access_token(refresh_token: schemas.RefreshToken):
    username = None
    try:
        payload = jwt.decode(
            refresh_token.refresh_token, 
            security.SECRET_KEY, 
            algorithms=[security.ALGORITHM]
            )
        username: str = payload.get('username')
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials',
                headers={'WWW-Authenticate': 'Bearer'}
                )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Signature has expired'
        )
        
    access_token = security.create_token(
        data={'username': username},
        expires_delta=timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {
        'token_type': 'Bearer', 
        'access_token': access_token,
    }


@app.get('/api/auth/current_user', response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
async def get_current_user(current_user: models.User = Depends(security.get_current_user)):
    return current_user
