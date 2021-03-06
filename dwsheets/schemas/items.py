from typing import List

from pydantic import BaseModel

from .tags import Tag


class Item(BaseModel):
    name: str
    tags: List[Tag]
