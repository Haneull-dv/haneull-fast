from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    user_id: str
    password: str

class LoginResponse(BaseModel):
    user_id: str
    name: Optional[str]
    email: Optional[str]
    access_token: str
    token_type: str = "bearer" 