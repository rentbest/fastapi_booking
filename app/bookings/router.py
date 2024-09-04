from fastapi import APIRouter, status

from app.bookings.schemes import BookingRequestScheme, BookingResponseScheme
from app.bookings.dao import BookingsDAO
import app.bookings.exceptions as exc
from app.rooms.dao import RoomsDAO
from app.users.dao import UsersDAO
from app.tasks.tasks import send_booking_confirmation_email

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", response_model=list[BookingResponseScheme])
async def get_bookings():
    bookings = await BookingsDAO.read_all()
    if not bookings:
        raise exc.BookingsNotFound
    return bookings


@router.get("/{booking_id}", response_model=BookingResponseScheme)
async def get_booking_by_id(booking_id: int):
    booking = await BookingsDAO.read_by_parameters(id=booking_id)
    if not booking:
        raise exc.BookingNotFound
    return booking[0]


@router.post("", response_model=BookingResponseScheme)
async def add_booking(booking_data: BookingRequestScheme):
    room = await RoomsDAO.read_by_parameters(id=booking_data.room_id)
    if not room:
        raise exc.BookingAddBadRequestRoom
    user = await UsersDAO.read_by_parameters(id=booking_data.user_id)
    if not user:
        raise exc.BookingAddBadRequestUser
    booking = await BookingsDAO.create(**booking_data.model_dump())
    if not booking:
        raise exc.BookingAddBadRequest

    booking_dict = {
        key: value for key, value in booking.__dict__.items() if not key.startswith("_")
    }
    # ВРЕМЕННАЯ ЗАГЛУШКА email_to !!!!!!!!!!!!!!!!!!!!
    send_booking_confirmation_email.delay(
        booking_dict, email_to="rinat.davleev.97@gmail.com"
    )
    return booking


@router.put("/{booking_id}", response_model=BookingResponseScheme)
async def update_booking(booking_id: int, booking_data: BookingRequestScheme):
    room = await RoomsDAO.read_by_parameters(id=booking_data.room_id)
    if not room:
        raise exc.BookingAddBadRequestRoom
    user = await UsersDAO.read_by_parameters(id=booking_data.user_id)
    if not user:
        raise exc.BookingAddBadRequestUser
    booking = await BookingsDAO.read_by_parameters(id=booking_id)
    if not booking:
        raise exc.BookingNotFound
    updated_booking = await BookingsDAO.update(
        id=booking_id, **booking_data.model_dump()
    )
    return updated_booking


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: int):
    booking = await BookingsDAO.read_by_parameters(id=booking_id)
    if not booking:
        raise exc.BookingNotFound
    await BookingsDAO.delete(booking_id)
    return None
