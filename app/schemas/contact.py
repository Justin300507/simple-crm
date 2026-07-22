from pydantic import BaseModel, Field
from typing import Optional, List

class ContactCreate(BaseModel):
    model_config = {"from_attributes": True}
    name: str = Field(min_length=1)
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    status: str = Field(min_length=1)

class ContactUpdate(BaseModel):
    model_config = {"from_attributes": True}
    name: Optional[str] = Field(min_length=1)
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = Field(min_length=1)

class ContactResponse(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None
    notes: List[str] = []
    interactions: List[str] = []

    class Config:
        from_attributes = True