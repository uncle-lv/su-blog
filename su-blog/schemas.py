from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    
    
class UserCreate(UserBase):
    password: str
    
    
class UserOut(UserBase):
    email: str
    avatar_url: str
    github_url: str
    qq: str
    
    class Config:
        orm_mode = True
        

class TokenBase(BaseModel):
    token_type: str
    

class RefreshToken(TokenBase):
    refresh_token: str
    
    
class TokenData(BaseModel):
    username: Optional[str] = None
    