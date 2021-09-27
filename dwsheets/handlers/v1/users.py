from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from dwsheets.config import Configuration as config
from dwsheets.database import db
from dwsheets.models.users import User
from dwsheets.schemas.users import User as UserSchema
from dwsheets.schemas.tokens import Token
from dwsheets.security import pwd_context
from dwsheets.security import create_access_token
from dwsheets.security import get_current_active_user

router = APIRouter()


@router.post('/token', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.fetch_one(select(User).where(User.username == form_data.username))
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/users/me', response_model=UserSchema)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
