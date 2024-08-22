from app.bookings.models import Booking
from app.dao.base import BaseDAO


class BookingsDAO(BaseDAO):
    model = Booking