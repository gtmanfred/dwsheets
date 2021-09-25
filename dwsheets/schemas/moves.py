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
    basic: str = 'basic'
    special: str = 'special'


class MoveType(str, Enum):
    choice: str = 'choice'
    starting: str = 'starting'
    advanced: str = 'advanced'


class BaseMove(BaseModel):
    name: str
    text: str
    move: MoveType 
    level: Optional[int]
    requires: Optional[str]


class Simple(BaseMove):
    type: Literal['simple']


class Class(BaseMove):
    type: Literal['class']
    classes: List[str]


class Choice(BaseMove):
    type: Literal['choice']
    num: int
    choices: List[str]


class Race(BaseMove):
    type: Literal['race']


class Move(BaseModel):
    __root__: Union[Simple, Class, Choice, Race] = Field(discriminator='type')
