from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import joinedload
from app.models.user_collection import UserCollection
from app.models.lego_set import LegoSet
from app.schemas.user_collection import UserCollectionCreate

async def get_collection(db: AsyncSession, user_id: str) -> list[UserCollection]:
    result = await db.execute(
        select(UserCollection)
        .where(UserCollection.user_id == user_id)
        .options(joinedload(UserCollection.lego_set))
        .order_by(UserCollection.id)
    )
    return result.scalars().all()

async def add_to_collection(
    db: AsyncSession,
    user_id: str,
    collection_in: UserCollectionCreate
) -> UserCollection:
    entry = UserCollection(user_id=user_id, **collection_in.model_dump())
    db.add(entry)
    await db.flush()
    await db.refresh(entry)
    return entry

async def get_collection_stats(db: AsyncSession, user_id: str) -> dict:
    result = await db.execute(
        select(
            func.count(UserCollection.id).label("total_sets"),
            func.sum(LegoSet.piece_count).label("total_pieces"),
            func.avg(LegoSet.piece_count).label("avg_pieces"),
            func.max(LegoSet.piece_count).label("max_pieces"),
        )
        .join(LegoSet, UserCollection.lego_set_id == LegoSet.id)
        .where(UserCollection.user_id == user_id)
    )
    row = result.first()
    return {
        "total_sets": row.total_sets or 0,
        "total_pieces": int(row.total_pieces or 0),
        "avg_pieces": round(float(row.avg_pieces or 0), 1),
        "largest_set_pieces": row.max_pieces or 0,
    }