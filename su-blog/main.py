from datetime import timedelta
from typing import List

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from starlette.status import HTTP_201_CREATED

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

@app.post('/api/oauth/access_token', status_code=status.HTTP_201_CREATED)
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


@app.post('/api/oauth/access_token/refresh', status_code=HTTP_201_CREATED)
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


@app.get('/api/oauth/current_user', response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
async def get_current_user(current_user: models.User = Depends(security.get_current_user)):
    return current_user


@app.patch('/api/oauth/pwd', status_code=status.HTTP_200_OK)
async def update_pwd(pwd: schemas.PwdBase, current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    crud.update_pwd(db, current_user.id, pwd.password)
    return


@app.put('/api/users', response_model=schemas.UserOut, status_code=status.HTTP_200_OK)
async def update_user(user: schemas.UserUpdate, current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    crud.update_user(db, current_user.id, user)
    return crud.get_user_by_id(db, current_user.id)


@app.get('/api/blogs', response_model=List[schemas.BlogOut], status_code=status.HTTP_200_OK)
async def get_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_blogs(db, skip, limit)


@app.get('/api/blogs/{id}', response_model=schemas.BlogOut, status_code=status.HTTP_200_OK)
async def get_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    blog = crud.get_blog_by_id(db, id)
    if blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    return blog


@app.post('/api/blogs', response_model=schemas.BlogOut, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: schemas.BlogCreate, current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    return crud.create_blog(db, blog)


@app.put('/api/blogs/{id}', response_model=schemas.BlogOut, status_code=status.HTTP_200_OK)
async def update_blog(blog: schemas.BlogUpdate, id: int, current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    db_blog = crud.get_blog_by_id(db, id)
    if db_blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    crud.update_blog(db, id,blog)
    return crud.get_blog_by_id(db, id)


@app.delete('/api/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def del_blog(id: int, current_user: models.User = Depends(security.get_current_user), db: Session = Depends(database.get_db)):
    db_blog = crud.get_blog_by_id(db, id)
    if db_blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    return crud.del_blog(db, id)
