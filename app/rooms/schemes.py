from pydantic import BaseModel


class RoomScheme(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list[str]
    quantity: int
    image_id: int

    class Config:
        from_attributes = True