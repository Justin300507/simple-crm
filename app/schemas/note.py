from typing import Optional
from pydantic import BaseModel


class NoteCreate(BaseModel):
    id: Optional[int] = None
    model_config = {'from_attributes': True}

