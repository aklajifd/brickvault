from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.theme import Theme
from app.schemas.theme import ThemeCreate

async def get_themes(db: AsyncSession) -> list[Theme]:
    result = await db.execute(select(Theme).order_by(Theme.name))
    return result.scalars().all()

async def get_theme_by_id(db: AsyncSession, theme_id: int) -> Theme | None:
    result = await db.execute(select(Theme).where(Theme.id == theme_id))
    return result.scalars().first()

async def create_theme(db: AsyncSession, theme_in: ThemeCreate) -> Theme:
    theme = Theme(**theme_in.model_dump())
    db.add(theme)
    await db.flush()
    await db.refresh(theme)
    return theme