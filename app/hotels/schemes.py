from pydantic import BaseModel, Field


class HotelSchemeRequest(BaseModel):
    name: str = Field(example="hotel name")
    location: str = Field(example="hotel location")
    services: list[str] = Field(example=['service1', 'service2'])
    rooms_quantity: int = Field(example=50, ge=1)
    image_id: int = Field(default=0, example=0)


    
class HotelSchemeResponse(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int