from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import constr

from .alignments import Alignment
from .items import Item
from .moves import Move
from .spells import Spell


class Choices(BaseModel):
    num: int
    options: List[List[Item]]


class Gear(BaseModel):
    load: int
    items: List[Item]
    choices: List[Choices]


class Spells(BaseModel):
    type: Union[Literal['learned'], Literal['granted']]
    spell_list: List[Spell]


class Class(BaseModel):
    name: str
    max_health_modifier: int
    base_damage: constr(regex=r'^d\d+$')  # noqa
    alignment: List[Alignment]
    gear: Gear
    bonds: List[str]
    moves: List[Move]
    spells: Optional[Spells]
