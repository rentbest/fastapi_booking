from fastapi import APIRouter

from app.hotels.schemes import HotelScheme
from app.hotels.dao import HotelsDAO
import app.hotels.exceptions as exc


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("", response_model=list[HotelScheme])
async def get_hotels():
    hotels = await HotelsDAO.find_all()
    if not hotels:
        raise exc.HotelsNotFound
    return hotels


@router.get("/{hotel_id}", response_model=HotelScheme)
async def get_hotel_by_id(hotel_id: int):
    hotel = await HotelsDAO.find_by_parameters(id=hotel_id)
    if not hotel:
        raise exc.HotelNotFound
    return hotel[0]
