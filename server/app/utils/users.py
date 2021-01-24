import random
import string
import os

from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt

from app.utils import firebase as firebase_utils


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = str(os.environ.get('SECRET_KEY'))
ALGORITHM = "HS256"


async def get_random_string(lenght=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(lenght))
    

def check_pass_len(password: str):
    if len(password) <= 6:
        return False    

def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)     


async def auth_user(phone: str, password: str):
    user = await firebase_utils.get_user(phone=phone)
    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user    

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt