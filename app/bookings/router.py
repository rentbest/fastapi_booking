from fastapi import APIRouter

from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.schemas import BookingScheme

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)

@router.get("", response_model=list[BookingScheme])
async def get_bookings():
    return await BookingDAO.find_all()


@router.get("/{booking_id}", response_model=list[BookingScheme])
async def get_bookings_by_id(booking_id: int):
    return await BookingDAO.find_by_parameters(id=booking_id)