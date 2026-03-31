from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Theme(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    rebrickable_id: Mapped[int | None] = mapped_column(Integer, nullable=True)

    sets: Mapped[list["LegoSet"]] = relationship(back_populates="theme")

    def __repr__(self) -> str:
        return f"<Theme {self.name}>"