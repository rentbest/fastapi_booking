from fastapi import APIRouter, status

from app.rooms.schemes import RoomRequestScheme, RoomResponseScheme
from app.rooms.dao import RoomsDAO
import app.rooms.exceptions as exc
from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix="/rooms",
    tags=["Номера"],
)


@router.get("", response_model=list[RoomResponseScheme])
async def get_rooms():
    rooms = await RoomsDAO.read_all()
    if not rooms:
        raise exc.RoomsNotFound
    return rooms


@router.get("/{room_id}", response_model=RoomResponseScheme)
async def get_room_by_id(room_id: int):
    room = await RoomsDAO.read_by_parameters(id=room_id)
    if not room:
        raise exc.RoomNotFound
    return room[0]


@router.post("", response_model=RoomResponseScheme)
async def add_room(room_data: RoomRequestScheme):
    hotel = await HotelsDAO.read_by_parameters(id=room_data.hotel_id)
    if not hotel:
        raise exc.RoomAddBadRequestHotel
    room = await RoomsDAO.create(**room_data.model_dump())
    if not room:
        raise exc.RoomAddBadRequest
    return room
    

@router.put("/{room_id}", response_model=RoomResponseScheme)
async def update_room(room_id: int, room_data: RoomRequestScheme):
    room = await RoomsDAO.read_by_parameters(id=room_id)
    if not room:
        raise exc.RoomNotFound
    updated_room = await RoomsDAO.update(id=room_id, **room_data.model_dump())
    return updated_room


@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(room_id: int):
    room = await RoomsDAO.read_by_parameters(id=room_id)
    if not room:
        raise exc.RoomNotFound
    await RoomsDAO.delete(room_id)
    return None