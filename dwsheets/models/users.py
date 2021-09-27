import uuid

from pydantic import EmailStr
from sqlmodel import Field
from sqlmodel import SQLModel

from ..schemas.users import User


class User(SQLModel, User, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password: bytes
