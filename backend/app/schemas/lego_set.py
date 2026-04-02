from pydantic import BaseModel, model_validator
from typing import Any

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
    
    @model_validator(mode="before")
    @classmethod
    def extract_theme_name(cls, values: Any) -> Any:
        if hasattr(values, "theme") and values.theme is not None:
            values.__dict__["theme_name"] = values.theme.name
        return values

