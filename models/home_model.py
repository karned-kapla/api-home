from pydantic import BaseModel, Field
from typing import Optional

class HomeBase(BaseModel):
    name: str
    description: Optional[str] = None

class HomeCreate(HomeBase):
    pass

class HomeCreateDatabase(HomeBase):
    created_by: Optional[str] = Field(None, description="User who created the home")

class HomeRead(HomeBase):
    uuid: str
    created_by: Optional[str] = Field(None, description="User who created the home")

class HomeUpdate(BaseModel):
    name: str
    description: Optional[str] = None
