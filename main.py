from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

app = FastAPI()
    

@app.get("/hotels")
def get_hotels(
    location: str, 
    date_from: date,
    date_to: date,
    stars: int = Query(None, ge=1, le=5, description="Stars must be between 1 and 5"),
    has_spa: bool = None):
    return location


class BookingScheme(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking_params: BookingScheme):
    return booking_params