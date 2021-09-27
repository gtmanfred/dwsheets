import uuid

from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    name: str
    disabled: bool = False
