from enum import Enum
from typing import List, Literal, Union

from pydantic import BaseModel
from pydantic import Field


class Quantity(BaseModel):
    type: Literal['quantity']
    modifier: int


class Applied(BaseModel):
    type: Literal['applied']


class Awkward(BaseModel):
    type: Literal['awkward']


class DurationEnum(str, Enum):
    ongoing: str = 'ongoing'
    forward: str = 'forward'

class Bonus(BaseModel):
    type: Literal['bonus']
    modifier: int
    options: DurationEnum


class Coins(BaseModel):
    type: Literal['coins']
    modifier: int


class Dangerous(BaseModel):
    type: Literal['dangerous']


class Uses(BaseModel):
    type: Literal['uses']
    modifier: int


class Weight(BaseModel):
    type: Literal['weight']
    modifier: int

class Hand(BaseModel):
    type: Literal['hand']


class Armor(BaseModel):
    type: Literal['armor']
    modifier: int


class Worn(BaseModel):
    type: Literal['worn']


class Close(BaseModel):
    type: Literal['close']


class Damage(BaseModel):
    type: Literal['damage']
    modifier: int


class Tag(BaseModel):
    __root__: Union[
        Applied,
        Armor,
        Awkward,
        Bonus,
        Close,
        Coins,
        Damage,
        Dangerous,
        Hand,
        Quantity,
        Uses,
        Weight,
        Worn,
    ] = Field(discriminator='type')
