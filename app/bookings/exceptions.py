from fastapi import HTTPException, status


class BaseException(HTTPException):
    """Base class for exceptions"""

    status_code = None
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class BookingNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Booking not found"


class BookingsNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Bookings not found"


class BookingAddBadRequest(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request for adding Booking"


class BookingAddBadRequestRoom(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request for adding Booking - Room not found"


class BookingAddBadRequestUser(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request for adding Booking - User not found"