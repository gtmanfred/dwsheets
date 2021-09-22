from pydantic import BaseModel


class Spell(BaseModel):
    name: str
    level: str
    text: str
