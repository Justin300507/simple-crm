from typing import Optional
from pydantic import BaseModel, Field

class StatsCreate(BaseModel):
    model_config = {"from_attributes": True}
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)

class StatsUpdate(BaseModel):
    model_config = {"from_attributes": True}
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)

class StatsResponse(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True