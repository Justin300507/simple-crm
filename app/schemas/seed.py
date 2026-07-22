from pydantic import BaseModel, Field

class SeedCreate(BaseModel):
    model_config = {"from_attributes": True}
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)

class SeedUpdate(BaseModel):
    model_config = {"from_attributes": True}
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)

class SeedResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True