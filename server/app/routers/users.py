from fastapi import APIRouter, HTTPException, status
from datetime import datetime, timedelta


from app.schemas import users as user_schemas
from app.utils import firebase as firebase_utils
from app.utils import users as user_utils


user_router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@user_router.post('/users/tel_check')
async def tel_check(phone: user_schemas.Phone):
    phone_check = await firebase_utils.check_phone(phone.phone)
    if phone_check == False:
        raise HTTPException(
           status_code=400,
           detail='Phone is already exist'
        )
    return HTTPException(
        status_code=200
    )    


@user_router.post('/users/singup')
async def create_user(user: user_schemas.UserCreate):
    password_chek = user_utils.check_pass_len(user.password)
    if password_chek == False:
        raise HTTPException(
            status_code=400,
            detail='incorect password'
            )

    phone_check = await firebase_utils.check_phone(user.phone)
    if phone_check == False:
        raise HTTPException(
           status_code=400,
           detail='Phone is already exist'
        )
    return await firebase_utils.create_user(user=user)


@user_router.post('/users/auth')
async def login_for_access_token(user: user_schemas.UserLogin):
    User = await user_utils.auth_user(user.phone, user.password)
    if not User:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect tel or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await user_utils.create_access_token(
        data={'sub': user.phone}, expires_delta=access_token_expires
    )    

    return [{ 'phone': User.phone, 'uid': User.uid}, {'access_token': access_token, 'token_type': 'bearer'}]