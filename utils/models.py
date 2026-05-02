from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Category(BaseModel):
    """Model for pet categories."""
    id: Optional[int] = None
    name: Optional[str] = None


class Tag(BaseModel):
    """Model for pet tags."""
    id: Optional[int] = None
    name: Optional[str] = None


class Pet(BaseModel):
    """Model for pet data."""
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None  # available, pending, sold


class Order(BaseModel):
    """Model for store orders."""
    id: Optional[int] = None
    petId: Optional[int] = None
    quantity: Optional[int] = None
    shipDate: Optional[datetime] = None
    status: Optional[str] = None  # placed, approved, delivered
    complete: Optional[bool] = None


class User(BaseModel):
    """Model for user accounts."""
    id: Optional[int] = None
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    userStatus: Optional[int] = None


class ApiResponse(BaseModel):
    """Model for API error responses."""
    code: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None
