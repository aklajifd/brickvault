from pydantic import BaseModel

class ThemeBase(BaseModel):
    name: str
    rebrickable_id: int | None = None

class ThemeCreate(ThemeBase):
    pass

class ThemeRead(ThemeBase):
    id: int

    model_config = {"from_attributes": True}