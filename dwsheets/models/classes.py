import uuid
from typing import Dict
from typing import List
from typing import TYPE_CHECKING

from sqlmodel import Column
from sqlmodel import Field
from sqlmodel import JSON
from sqlmodel import Relationship
from sqlmodel import String
from sqlmodel import SQLModel

if TYPE_CHECKING:
    from .spells import Spell
    from .moves import Move


class Class(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    classobj: Dict = Field(sa_column=Column(JSON))
    name: str = Field(sa_column=Column(String, unique=True, nullable=False))
    spells: List["Spell"] = Relationship(back_populates="classobj")
    moves: List["Move"] = Relationship(back_populates="classobj")
