import uuid
from typing import List
from typing import Optional

import fastapi
from sqlmodel import select
from sqlmodel import Integer
from sqlmodel.ext.asyncio.session import AsyncSession

from dwsheets.database import db
from dwsheets.models.spells import Spell

router = fastapi.APIRouter()


@router.get('/spells', response_model=List[Spell])
async def get_spells(
    request: fastapi.Request,
    classes: Optional[List[uuid.UUID]] = None
):
    query = select(Spell)
    if classes is not None:
        query = query.where(Spell.class_uid.in_(classes))
    spells = await db.execute(query)
    return await spells.fetch_all()


@router.get('/spells/{spell_uid}/spell', response_model=Spell)
async def get_spell(request: fastapi.Request, spell_uid: uuid.UUID):
    return await db.fetch_one(select(Spell).where(Spell.uid == spell_uid))
