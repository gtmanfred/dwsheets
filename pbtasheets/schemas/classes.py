from enum import Enum
from typing import List

from pydantic import BaseModel
from pydantic import constr

from .alignments import Alignment
from .items import Item
from .moves import Move


class Choices(BaseModel):
    num: int
    options: List[List[Item]]


class Gear(BaseModel):
    load: int
    items: List[Item]
    choices: List[Choices]


class Class(BaseModel):
    name: str
    max_health_modifier: int
    base_damage: constr(regex='^d\d+')
    alignment: List[Alignment]
    gear: Gear
    bonds: List[str]
    moves: List[Move]
