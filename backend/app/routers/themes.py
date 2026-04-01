from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.theme import ThemeCreate, ThemeRead
from app.crud.theme import get_themes, get_theme_by_id, create_theme
from app.crud.lego_set import get_sets_by_theme
from app.schemas.lego_set import LegoSetRead

router = APIRouter(prefix="/themes", tags=["themes"])

@router.get("/", response_model=list[ThemeRead])
async def list_themes(db: AsyncSession = Depends(get_db)):
    return await get_themes(db)

@router.get("/{theme_id}", response_model=ThemeRead)
async def get_theme(theme_id: int, db: AsyncSession = Depends(get_db)):
    theme = await get_theme_by_id(db, theme_id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return theme

@router.get("/{theme_id}/sets", response_model=list[LegoSetRead])
async def list_sets_by_theme(theme_id: int, db: AsyncSession = Depends(get_db)):
    theme = await get_theme_by_id(db, theme_id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return await get_sets_by_theme(db, theme_id)

@router.post("/", response_model=ThemeRead, status_code=201)
async def create_new_theme(theme_in: ThemeCreate, db: AsyncSession = Depends(get_db)):
    return await create_theme(db, theme_in)