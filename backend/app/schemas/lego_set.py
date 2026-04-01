from pydantic import BaseModel

class LegoSetBase(BaseModel):
    set_number: str
    name: str
    year: int | None = None
    piece_count: int | None = None
    image_url: str | None = None
    theme_id: int | None = None

class LegoSetCreate(LegoSetBase):
    pass

class LegoSetRead(LegoSetBase):
    id: int
    theme_name: str | None = None

    model_config = {"from_attributes": True}

