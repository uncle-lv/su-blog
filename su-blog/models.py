from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, DateTime, Text
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True, nullable=False)
    avatar_url = Column(Text, nullable=False)
    github_url = Column(Text, nullable=True)
    qq = Column(String(32), nullable=True)
    password = Column(String(128), nullable=False)
    created_time = Column(DateTime, nullable=False)
    last_login = Column(DateTime, nullable=True)
   
    
class Blog(Base):
    __tablename__ = 'blog'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    chief_description = Column(String(256), nullable=False)
    content = Column(Text, nullable=False)
    created_time = Column(DateTime, nullable=False)
    modified_time = Column(DateTime)
