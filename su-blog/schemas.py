from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    
    
class UserCreate(UserBase):
    password: str
    
    
class UserOut(UserBase):
    email: EmailStr
    avatar_url: str
    github_url: str
    qq: str
    
    class Config:
        orm_mode = True
        

class UserUpdate(UserOut):
    pass
        

class TokenBase(BaseModel):
    token_type: str
    

class RefreshToken(TokenBase):
    refresh_token: str
    
    
class TokenData(BaseModel):
    username: Optional[str] = None
    

class PwdBase(BaseModel):
    password: str
    
    
class BlogBase(BaseModel):
    title: str
    chief_description: str
    content: str
    
    
class BlogCreate(BlogBase):
    pass


class BlogOut(BlogBase):
    id: int
    created_time: datetime
    modified_time: Optional[datetime] = None
    
    class Config:
        orm_mode = True
        
        
class BlogUpdate(BlogBase):
    pass
    