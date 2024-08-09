from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: int = Query(
            None, ge=1, le=5, description="Stars must be between 1 and 5"),
        has_spa: bool = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get("/hotels")
def get_hotels(hotel_search_args: HotelSearchArgs = Depends()):
    return hotel_search_args


class BookingScheme(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking_params: BookingScheme):
    return booking_params
