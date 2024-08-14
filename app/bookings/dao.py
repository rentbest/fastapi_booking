from app.bookings.models import Booking
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Booking