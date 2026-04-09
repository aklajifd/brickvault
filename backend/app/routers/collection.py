from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user_collection import UserCollectionCreate, UserCollectionRead
from app.crud.user_collection import get_collection, add_to_collection, get_collection_stats
from app.crud.lego_set import get_set_by_id
from app.core.security import get_current_user

router = APIRouter(prefix="/collection", tags=["collection"])

@router.get("/me", response_model=list[UserCollectionRead])
async def list_collection(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    return await get_collection(db, user_id)

@router.get("/me/stats")
async def collection_stats(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    return await get_collection_stats(db, user_id)

@router.get("/me/wishlist", response_model=list[UserCollectionRead])
async def list_wishlist(
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    collection = get_collection(db, user_id)
    return [entry for entry in collection if entry.is_wishlist]

@router.post("/me", response_model=UserCollectionRead, status_code=201)
async def add_set_to_collection(
    collection_in: UserCollectionCreate,
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    lego_set = await get_set_by_id(db, collection_in.lego_set_id)
    if not lego_set:
        raise HTTPException(status_code=404, detail="Set not found")
    return await add_to_collection(db, user_id, collection_in)

@router.delete("/me/{entry_id}", status_code=204)
async def remove_from_collection(
    entry_id: int, 
    db: AsyncSession = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    raise HTTPException(status_code=501, detail="Coming soon")