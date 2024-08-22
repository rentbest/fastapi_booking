from fastapi import APIRouter, HTTPException

from app.users.schemes import UserAuthSchema
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Авторизация"],
)


@router.post("/register")
async def register_user(user_data: UserAuthSchema):
    is_user_exists = await UserDAO.read_by_parameters(email=user_data.email)
    if is_user_exists:
        raise HTTPException(status_code=409)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.create(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(user_data: UserAuthSchema):
    user = await UserDAO.read_by_parameters(email=user_data.email)
    if not user:
        raise HTTPException(status_code=401)
    is_password_valid = verify_password(user_data.password, user.password)
    if not is_password_valid:
        raise HTTPException(status_code=401)