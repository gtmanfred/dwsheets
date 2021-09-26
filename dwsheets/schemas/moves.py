from enum import Enum
from typing import Annotated
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
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
    basic: str = 'basic'
    special: str = 'special'


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


Move = Annotated[
    Union[tuple(BaseMove.__subclasses__())],
    Field(discriminator='type'),
]
