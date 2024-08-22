from pydantic import BaseModel, EmailStr, Field


class UserAuthSchema(BaseModel):
    email: EmailStr
    password: str
