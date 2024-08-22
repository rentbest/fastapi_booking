from pydantic import BaseModel, Field


class RoomRequestScheme(BaseModel):
    hotel_id: int = Field(example=1)
    name: str = Field(default="Econom", example="room name")
    description: str = Field(example="room desciption")
    price: int = Field(default=2000, example=1000, ge=0)
    services: list[str] = Field(example=["Shower", "TV", "A/C"])
    quantity: int = Field(default=30, example=50)
    image_id: int = Field(default=0, example=0)


class RoomResponseScheme(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int