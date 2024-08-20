from app.dao.base import BaseDAO
from app.hotels.models import Hotel


class HotelsDAO(BaseDAO):
    model = Hotel