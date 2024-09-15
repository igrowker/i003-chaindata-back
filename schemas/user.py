from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    user_id: int | None = None
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        
class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
