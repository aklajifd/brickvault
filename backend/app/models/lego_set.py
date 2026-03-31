from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class LegoSet(Base):
    __tablename__ = "lego_sets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    set_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    piece_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    image_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    theme_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("themes.id"), nullable=True)

    theme: Mapped["Theme | None"] = relationship(back_populates="sets")
    collection_entries: Mapped[list["UserCollection"]] = relationship(back_populates="lego_set")

    def __repr__(self) -> str:
        return f"<LegoSet {self.set_number} - {self.name}>"