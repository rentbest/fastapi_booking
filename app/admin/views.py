from sqladmin import ModelView

from app.users.models import User
from app.hotels.models import Hotel


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class HotelAdmin(ModelView, model=Hotel):
    column_list = [c.name for c in Hotel.__table__.c]
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"
