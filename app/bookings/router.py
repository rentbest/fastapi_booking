from fastapi import APIRouter
from app.database import async_session
from app.bookings import Boo


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings():
    async with async_session() as session:
        # query = select(Bookings)
        pass


@router.get("/{booking_id}")
async def get_bookings_by_id(booking_id: int):
    pass