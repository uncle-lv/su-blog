from datetime import datetime

from sqlalchemy.orm import Session

import models


def get_user_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id==id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email==email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username==username).first()

def update_last_login(db: Session, id: int):
    db.query(models.User).filter(models.User.id==id).update(dict(last_login=datetime.utcnow()))
    db.commit()
