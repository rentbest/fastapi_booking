from pydantic import BaseModel, Field


class HotelScheme(BaseModel):
    name: str = Field(example=1)
    location: str = Field(example=1)
    services: list[str] = Field(example=['service1', 'service2'])
    rooms_quantity: int = Field(example=1)
    image_id: int = Field(example=1)
    
    class Config:
        from_attributes = True
