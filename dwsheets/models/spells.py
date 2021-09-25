import uuid
from typing import Dict
from typing import TYPE_CHECKING

from sqlmodel import Column
from sqlmodel import Field
from sqlmodel import JSON
from sqlmodel import Relationship
from sqlmodel import String
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .classes import Class


class Spell(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    spell: Dict = Field(sa_column=Column(JSON))
    name: str = Field(sa_column=Column(String, unique=True, nullable=False))
    class_uid: uuid.UUID = Field(default=None, foreign_key='class.uid')
    classobj: "Class" = Relationship(back_populates='spells')
