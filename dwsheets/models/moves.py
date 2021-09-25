import uuid
from typing import Dict
from typing import TYPE_CHECKING
from typing import Optional

from sqlmodel import Column
from sqlmodel import Enum
from sqlmodel import Field
from sqlmodel import JSON
from sqlmodel import Relationship
from sqlmodel import String
from sqlmodel import SQLModel

from ..schemas.moves import MoveType

if TYPE_CHECKING:
    from .classes import Class


class Move(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    move: Dict = Field(sa_column=Column(JSON))
    name: str = Field(sa_column=Column(String, unique=True, nullable=False))
    type: MoveType = Field(sa_column=Column(Enum(MoveType), nullable=False))
    class_uid: uuid.UUID = Field(default=None, foreign_key='class.uid')
    classobj: Optional["Class"] = Relationship(back_populates='moves')
