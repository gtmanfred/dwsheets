import uuid
from typing import List
from typing import Optional

import fastapi
from sqlalchemy.orm import joinedload
from sqlmodel import select
from sqlmodel import Integer
from sqlmodel.ext.asyncio.session import AsyncSession

from dwsheets.database import db
from dwsheets.models.moves import Move

router = fastapi.APIRouter()


@router.get('/moves', response_model=List[Move])
async def get_moves(
    request: fastapi.Request,
    min_level: Optional[int] = None,
    classes: Optional[List[uuid.UUID]] = None
):
    query = select(Move)
    if min_level is not None:
        query = query.where(
            Move.move['level'].cast(Integer) >= min_level,
        )
    if classes is not None:
        query = query.where(Move.class_uid.in_(classes))
    return await db.fetch_all(query)


@router.get('/moves/{move_uid}/move', response_model=Move)
async def get_move(request: fastapi.Request, move_uid: uuid.UUID):
    moves = await db.execute(select(Move).where(Move.uid == move_uid))
    return moves.fetch_one()
