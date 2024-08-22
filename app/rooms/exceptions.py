from fastapi import HTTPException, status


class BaseException(HTTPException):
    """Base class for exceptions"""

    status_code = None
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class RoomNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Room not found"


class RoomsNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Rooms not found"


class RoomAddBadRequest(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request for adding Room"


class RoomAddBadRequestHotel(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request for adding Room - Hotel does not exist"
