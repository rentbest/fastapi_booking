from app.dao.base import BaseDAO
from app.rooms.models import Room


class RoomsDAO(BaseDAO):
    model = Room
