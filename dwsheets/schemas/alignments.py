from enum import Enum

from pydantic import BaseModel


class AlignmentsEnum(str, Enum):
    neutral: str = 'neutral'
    chaotic: str = 'chaotic'
    evil: str = 'evil'
    lawful: str = 'lawful'
    good: str = 'good'


class Alignment(BaseModel):
    type: AlignmentsEnum
    text: str
