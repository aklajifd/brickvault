from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user_collection import UserCollectionCreate, UserCollectionRead
from app.crud.user_collection import get_collection, add_to_collection, get_collection_stats
from app.crud.lego_set import get_set_by_id

router = APIRouter(prefix="/collection", tags=["collection"])

TEMP_USER_ID = "daniel"

@router.get("/me", response_model=list[UserCollectionRead])
async def list_collection(db: AsyncSession = Depends(get_db)):
    return await get_collection(db, TEMP_USER_ID)

@router.get("/me/stats")
async def collection_stats(db: AsyncSession = Depends(get_db)):
    return await get_collection_stats(db, TEMP_USER_ID)

@router.get("/me/wishlist", response_model=list[UserCollectionRead])
async def list_wishlist(db: AsyncSession = Depends(get_db)):
    collection = get_collection(db, TEMP_USER_ID)
    return [entry for entry in collection if entry.is_wishlist]

@router.post("/me", response_model=UserCollectionRead, status_code=201)
async def add_set_to_collection(
    collection_in: UserCollectionCreate,
    db: AsyncSession = Depends(get_db)
):
    lego_set = await get_set_by_id(db, collection_in.lego_set_id)
    if not lego_set:
        raise HTTPException(status_code=404, detail="Set not found")
    return await add_to_collection(db, TEMP_USER_ID, collection_in)

@router.delete("/me/{entry_id}", status_code=204)
async def remove_from_collection(entry_id: int, db: AsyncSession = Depends(get_db)):
    raise HTTPException(status_code=501, detail="Coming soon")