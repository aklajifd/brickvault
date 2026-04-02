from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.lego_set import LegoSetCreate, LegoSetRead
from app.crud.lego_set import get_sets, get_set_by_id, get_set_by_number, create_set

router = APIRouter(prefix="/sets", tags=["sets"])

@router.get("/", response_model=list[LegoSetRead])
async def list_sets(db: AsyncSession = Depends(get_db)):
    return await get_sets(db)

@router.get("/{set_id}", response_model=LegoSetRead)
async def get_set(set_id: int, db: AsyncSession = Depends(get_db)):
    lego_set = await get_set_by_id(db, set_id)
    if not lego_set:
        raise HTTPException(status_code=404, detail="Set not found")
    return lego_set

@router.post("/", response_model=LegoSetRead, status_code=201)
async def create_new_set(set_in: LegoSetCreate, db: AsyncSession = Depends(get_db)):
    existing = await get_set_by_number(db, set_in.set_number)
    if existing:
        raise HTTPException(status_code=400, detail="Set number already exists")
    return await create_set(db, set_in)

@router.post("/lookup/{set_number}", response_model=LegoSetRead, status_code=201)
async def lookup_and_create_set(set_number: str, db: AsyncSession = Depends(get_db)):
    existing = await get_set_by_number(db, set_number)
    if existing:
        return existing
    raise HTTPException(status_code=501, detail="Rebrickable integration coming soon")