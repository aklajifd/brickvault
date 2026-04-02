from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.models.lego_set import LegoSet
from app.schemas.lego_set import LegoSetCreate

async def get_sets(db: AsyncSession) -> list[LegoSet]:
    result = await db.execute(
        select(LegoSet)
        .options(joinedload(LegoSet.theme))
        .order_by(LegoSet.name)
    )
    return result.scalars().all()

async def get_set_by_id(db: AsyncSession, set_id: int) -> LegoSet | None:
    result = await db.execute(
        select(LegoSet)
        .options(joinedload(LegoSet.theme))
        .where(LegoSet.id == set_id)
    )
    return result.scalars().first()

async def get_set_by_number(db: AsyncSession, set_number: str) -> LegoSet | None:
    result = await db.execute(
        select(LegoSet)
        .options(joinedload(LegoSet.theme))
        .where(LegoSet.set_number == set_number)
    )
    return result.scalars().first()

async def create_set(db: AsyncSession, set_in: LegoSetCreate) -> LegoSet:
    lego_set = LegoSet(**set_in.model_dump())
    db.add(lego_set)
    await db.flush()
    result = await db.execute(
        select(LegoSet)
        .options(joinedload(LegoSet.theme))
        .where(LegoSet.id == lego_set.id)
    )
    return result.scalars().first()

async def get_sets_by_theme(db: AsyncSession, theme_id: int) -> list[LegoSet]:
    result = await db.execute(
        select(LegoSet)
        .options(joinedload(LegoSet.theme))
        .where(LegoSet.theme_id == theme_id)
        .order_by(LegoSet.name)
    )
    return result.scalars().all()