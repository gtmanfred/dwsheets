import uuid

from sqlmodel import Field
from sqlmodel import SQLModel


class Campaign(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_uid: uuid.UUID = Field(default=None, foreign_key='user.uid')
