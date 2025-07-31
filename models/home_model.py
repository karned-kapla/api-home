from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any

class HomeRead(BaseModel):
    uuid: str
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    number_of_persons: Optional[int] = Field(None, gt=0, description="Number of persons the home serves")
    origin_country: Optional[str] = None
    attributes: List[str] = Field(default_factory=list, description="Attributes like vegetarian, gluten-free, etc.")
    utensils: List[str] = Field(default_factory=list, description="List of utensils needed for the home")
    ingredients: List[Dict[str, Any]] = Field(default_factory=list, description="List of ingredients with their quantities")
    steps: List[Dict[str, Any]] = Field(default_factory=list, description="List of steps to prepare the home")
    thumbnail_url: Optional[HttpUrl] = Field(None, description="URL for the home thumbnail image")
    large_image_url: Optional[HttpUrl] = Field(None, description="URL for a larger image of the home")
    source_reference: Optional[str] = Field(None, description="Reference for the source of the home (e.g., book, website)")
    created_by: Optional[str] = Field(None, description="User who created the home")

class HomeWrite(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    number_of_persons: Optional[int] = Field(None, gt=0, description="Number of persons the home serves")
    origin_country: Optional[str] = None
    attributes: List[str] = Field(default_factory=list, description="Attributes like vegetarian, gluten-free, etc.")
    utensils: List[str] = Field(default_factory=list, description="List of utensils needed for the home")
    ingredients: List[Dict[str, Any]] = Field(default_factory=list, description="List of ingredients with their quantities")
    steps: List[Dict[str, Any]] = Field(default_factory=list, description="List of steps to prepare the home")
    thumbnail_url: Optional[HttpUrl] = Field(None, description="URL for the home thumbnail image")
    large_image_url: Optional[HttpUrl] = Field(None, description="URL for a larger image of the home")
    source_reference: Optional[str] = Field(None, description="Reference for the source of the home (e.g., book, website)")
    created_by: Optional[str] = Field(None, description="User who created the home")
