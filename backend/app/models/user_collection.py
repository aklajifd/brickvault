from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class UserCollection(Base):
    __tablename__ = "user_collections"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    lego_set_id: Mapped[int] = mapped_column(Integer, ForeignKey("lego_sets.id"), nullable=False)
    is_wishlist: Mapped[bool] = mapped_column(Boolean, default=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    lego_set: Mapped["LegoSet"] = relationship(back_populates="collection_entries")

    def __repr__(self) -> str:
        return f"<UserCollection user={self.user_id} set={self.lego_set_id}>"