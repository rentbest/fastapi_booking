from fastapi import APIRouter, HTTPException

from app.users.schemas import UserRegisterSchema
from app.users.dao import UserDAO
from app.users.auth import get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Авторизация"],
)


@router.post("/register")
async def register_user(user_data: UserRegisterSchema):
    is_user_exists = await UserDAO.find_by_parameters(email=user_data.email)
    if is_user_exists:
        raise HTTPException(status_code=409)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)