from pydantic import BaseModel, Field
from datetime import date


class BookingRequestScheme(BaseModel):
    room_id: int = Field(..., example=1, description="ID комнаты, которую бронируют")
    user_id: int = Field(
        ..., example=1, description="ID пользователя, который совершает бронирование"
    )
    date_from: date = Field(
        ..., example="2024-09-01", description="Дата начала бронирования"
    )
    date_to: date = Field(
        ..., example="2024-09-07", description="Дата окончания бронирования"
    )
    price: int = Field(..., example=100, description="Цена за ночь проживания")


class BookingResponseScheme(BaseModel):
    id: int = Field(..., example=1, description="ID бронирования")
    room_id: int = Field(..., example=1, description="ID комнаты, которую бронируют")
    user_id: int = Field(
        ..., example=1, description="ID пользователя, который совершает бронирование"
    )
    date_from: date = Field(
        ..., example="2024-09-01", description="Дата начала бронирования"
    )
    date_to: date = Field(
        ..., example="2024-09-07", description="Дата окончания бронирования"
    )
    price: int = Field(..., example=100, description="Цена за ночь проживания")
    total_cost: int = Field(
        ..., example=600, description="Общая стоимость бронирования"
    )
    total_days: int = Field(
        ..., example=6, description="Общее количество дней проживания"
    )
