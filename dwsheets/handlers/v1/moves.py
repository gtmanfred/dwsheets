import uuid
from typing import List
from typing import Optional

import fastapi
from sqlmodel import select
from sqlmodel import Integer
from sqlmodel.ext.asyncio.session import AsyncSession

from dwsheets.models.moves import Move

router = fastapi.APIRouter()


@router.get('/moves', response_model=List[Move])
async def get_moves(
    request: fastapi.Request,
    min_level: Optional[int] = None,
    classes: Optional[List[uuid.UUID]] = None
):
    async with AsyncSession(request.app.state.engine) as session:
        query = select(Move)
        if min_level is not None:
            query = query.where(
                Move.move['level'].cast(Integer) >= min_level,
            )
        if classes is not None:
            query = query.where(Move.class_uid.in_(classes))
        moves = await session.exec(query)
        return moves.all()


@router.get('/moves/{move_uid}/move', response_model=Move)
async def get_move(request: fastapi.Request, move_uid: uuid.UUID):
    async with AsyncSession(request.app.state.engine) as session:
        moves = await session.exec(select(Move).where(Move.uid == move_uid))
        return moves.first()
