from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str] = None
    password: str
    phone: str

class UserLogin(BaseModel):
    phone: str
    password: str

class UserOut(UserLogin):
    uid: str

class Phone(BaseModel):
    phone: str  