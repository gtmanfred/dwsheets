from enum import Enum
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic.errors import NumberNotGeError


class Type(str, Enum):
    simple: str = 'simple'
    cls: str = 'class'
    choice: str = 'choice'
    race: str = 'race'


class How(str, Enum):
    choice: str = 'choice'
    starting: str = 'starting'
    advanced: str = 'advanced'


class Move(BaseModel):
    name: str
    text: str
    type: Type
    how: How
    num: int
    choices: List[str]
    level: Optional[int]
    requires: str
