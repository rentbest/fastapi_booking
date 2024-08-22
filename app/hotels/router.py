from fastapi import APIRouter, status

from app.hotels.schemes import HotelRequestScheme, HotelResponseScheme
from app.hotels.dao import HotelsDAO
import app.hotels.exceptions as exc


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("", response_model=list[HotelResponseScheme])
async def get_hotels():
    hotels = await HotelsDAO.read_all()
    if not hotels:
        raise exc.HotelsNotFound
    return hotels


@router.get("/{hotel_id}", response_model=HotelResponseScheme)
async def get_hotel_by_id(hotel_id: int):
    hotel = await HotelsDAO.read_by_parameters(id=hotel_id)
    if not hotel:
        raise exc.HotelNotFound
    return hotel[0]


@router.post("", response_model=HotelResponseScheme)
async def add_hotel(hotel_data: HotelRequestScheme):
    hotel = await HotelsDAO.create(**hotel_data.model_dump())
    if not hotel:
        raise exc.HotelAddBadRequest
    return hotel
    

@router.put("/{hotel_id}", response_model=HotelResponseScheme)
async def update_hotel(hotel_id: int, hotel_data: HotelRequestScheme):
    hotel = await HotelsDAO.read_by_parameters(id=hotel_id)
    if not hotel:
        raise exc.HotelNotFound
    updated_hotel = await HotelsDAO.update(id=hotel_id, **hotel_data.model_dump())
    return updated_hotel


@router.delete("/{hotel_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hotel(hotel_id: int):
    hotel = await HotelsDAO.read_by_parameters(id=hotel_id)
    if not hotel:
        raise exc.HotelNotFound
    await HotelsDAO.delete(hotel_id)
    return None