from enum import Enum
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic.errors import NumberNotGeError
from pydantic.fields import Field


class SelectType(str, Enum):
    simple: str = 'simple'
    cls: str = 'class'
    choice: str = 'choice'
    race: str = 'race'


class MoveType(str, Enum):
    choice: str = 'choice'
    starting: str = 'starting'
    advanced: str = 'advanced'


class Simple(BaseModel):
    type: Literal['simple']
    name: str
    text: str
    move: MoveType 
    level: Optional[int]
    requires: Optional[str]


class Class(BaseModel):
    type: Literal['class']
    name: str
    text: str
    move: MoveType 
    level: Optional[int]
    requires: Optional[str]
    classes: List[str]


class Choice(BaseModel):
    type: Literal['choice']
    name: str
    text: str
    move: MoveType 
    level: Optional[int]
    requires: Optional[str]
    num: int
    choices: List[str]


class Race(BaseModel):
    type: Literal['race']
    name: str
    text: str
    move: MoveType 
    level: Optional[int]
    requires: Optional[str]


class Move(BaseModel):
    __root__: Union[Simple, Class, Choice, Race] = Field(discriminator='type')
