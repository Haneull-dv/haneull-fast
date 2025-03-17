from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: Optional[str] = None
    
    class Config:
        from_attributes = True

class MemberCreate(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: str
    
    class Config:
        from_attributes = True

class MemberResponse(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: Optional[str] = None
    
    class Config:
        from_attributes = True