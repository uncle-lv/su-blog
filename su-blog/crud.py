from datetime import datetime

from sqlalchemy.orm import Session

import models, security, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id==id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email==email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username==username).first()

def update_last_login(db: Session, id: int):
    db.query(models.User).filter(models.User.id==id).update(dict(last_login=datetime.utcnow()))
    db.commit()
    
def update_pwd(db: Session, id: int, password: str):
    hashed_pwd = security.hash_pwd(password)
    db.query(models.User).filter(models.User.id==id).update(dict(password=hashed_pwd))
    db.commit()
    
def update_user(db: Session, id: int, user: schemas.UserUpdate):
    db.query(models.User).filter(models.User.id==id).update(dict(
        username=user.username, 
        email=user.email, 
        avatar_url=user.avatar_url, 
        github_url=user.github_url, 
        qq=user.qq
        ))
    db.commit()
    
def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def get_blog_by_id(db: Session, id: int):
    return db.query(models.Blog).filter(models.Blog.id==id).first()
    
def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(
        title=blog.title, 
        chief_description=blog.chief_description, 
        content=blog.content, 
        created_time=datetime.utcnow()
        )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, id: int, blog: schemas.BlogUpdate):
    db.query(models.Blog).filter(models.Blog.id==id).update(dict(
        title=blog.title, 
        chief_description=blog.chief_description, 
        content=blog.content, 
        modified_time=datetime.utcnow()
        ))
    db.commit()

def del_blog(db: Session, id: int):
    db.query(models.Blog).filter(models.Blog.id==id).delete()
    db.commit()
