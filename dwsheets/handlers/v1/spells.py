import uuid
from typing import List
from typing import Optional

import fastapi
from sqlmodel import select
from sqlmodel import Integer
from sqlmodel.ext.asyncio.session import AsyncSession

from dwsheets.models.spells import Spell

router = fastapi.APIRouter()


@router.get('/spells', response_model=List[Spell])
async def get_spells(
    request: fastapi.Request,
    classes: Optional[List[uuid.UUID]] = None
):
    async with AsyncSession(request.app.state.engine) as session:
        query = select(Spell)
        if classes is not None:
            query = query.where(Spell.class_uid.in_(classes))
        spells = await session.exec(query)
        return spells.all()


@router.get('/spells/{spell_uid}/spell', response_model=Spell)
async def get_spell(request: fastapi.Request, spell_uid: uuid.UUID):
    async with AsyncSession(request.app.state.engine) as session:
        spells = await session.exec(select(Spell).where(Spell.uid == spell_uid))
        return spells.first()
