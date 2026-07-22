from pydantic import BaseModel, Field
from typing import Optional, List

class UserCreate(BaseModel):
    model_config = {"from_attributes": True}
    email: str = Field(min_length=1)
    password_hash: str = Field(min_length=1)

class UserUpdate(BaseModel):
    model_config = {"from_attributes": True}
    email: Optional[str] = Field(None, min_length=1)
    password_hash: Optional[str] = Field(None, min_length=1)

class UserResponse(BaseModel):
    id: int
    email: Optional[str] = None
    contacts: List[Optional[str]] = []  # Assuming contacts are represented as a list of strings

    class Config:
        from_attributes = True

