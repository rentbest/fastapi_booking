from fastapi import HTTPException, status


class BaseException(HTTPException):
    """Base class for exceptions"""

    status_code = None
    detail = None

    def __init__(self) -> HTTPException:
        super().__init__(status_code=self.status_code, detail=self.detail)


class HotelNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Hotel not found"

class HotelsNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Hotels not found"