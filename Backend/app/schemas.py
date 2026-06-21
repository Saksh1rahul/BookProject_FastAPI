from pydantic import BaseModel, ConfigDict, field_validator,Field
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    publisher: str
    name: str
    date: date
    Cost: float = Field(gt=0)
    @field_validator("date")
    @classmethod
    def validate_date(cls, value):
        if value > date.today():
            raise ValueError(
                "Future dates are not allowed"
            )
        return value
   
    

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    owner_id: int
    owner: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    id: int
    username: str
    token: str

    model_config = ConfigDict(from_attributes=True)
