import uuid
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    name: Optional[str]
    disabled: bool = False


class LoginUser(BaseModel):
    username: Union[str, EmailStr]
    password: bytes
