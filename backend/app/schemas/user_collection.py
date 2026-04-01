from pydantic import BaseModel
from app.schemas.lego_set import LegoSetRead

class UserCollectionBase(BaseModel):
    lego_set_id: int
    is_wishlist: bool = False
    quantity: int = 1

class UserCollectionCreate(UserCollectionBase):
    pass

class UserCollectionRead(UserCollectionBase):
    id: int
    lego_set: LegoSetRead

    model_config = {"from_attributes:": True}