import uuid

from sqlmodel import Field
from sqlmodel import SQLModel


class Character(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    class_uid: uuid.UUID = Field(default=None, foreign_key='class.uid')
    owner_uid: uuid.UUID = Field(default=None, foreign_key='user.uid')
    campaign_uid: uuid.UUID = Field(default=None, foreign_key='campaign.uid')
