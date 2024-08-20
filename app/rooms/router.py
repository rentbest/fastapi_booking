from fastapi import APIRouter

from app.rooms.schemes import RoomScheme
from app.rooms.dao import RoomsDAO
import app.rooms.exceptions as exc


router = APIRouter(
    prefix="/rooms",
    tags=["Номера"]
)


@router.get("", response_model=list[RoomScheme])
async def get_rooms():
    rooms = await RoomsDAO.find_all()
    if not rooms:
        raise exc.RoomsNotFound
    return rooms


@router.get("/{room_id}", response_model=RoomScheme)
async def get_room_by_id(room_id: int):
    room = await RoomsDAO.find_by_parameters(id=room_id)
    if not room:
        raise exc.RoomNotFound
    return room
