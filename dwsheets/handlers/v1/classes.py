import uuid
from typing import List
from typing import Optional

import fastapi
from sqlmodel import select
from sqlmodel import Integer
from sqlmodel.ext.asyncio.session import AsyncSession

from dwsheets.database import db
from dwsheets.models.classes import Class

router = fastapi.APIRouter()


@router.get('/classes', response_model=List[Class])
async def get_classs(
    request: fastapi.Request,
    min_level: Optional[int] = None,
    classes: Optional[List[uuid.UUID]] = None
):
    return await db.fetch_all(select(Class))


@router.get('/classes/{class_uid}/class', response_model=Class)
async def get_class(request: fastapi.Request, class_uid: uuid.UUID):
    return await db.fetch_one(select(Class).where(Class.uid == class_uid))
