from pydantic import BaseModel, EmailStr


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str