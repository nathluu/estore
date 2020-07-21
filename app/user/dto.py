from pydantic import BaseModel


class UserDtoIn(BaseModel):
    username: str
    password: str
    email: str = None
    phone: str = None
    first_name: str = None
    last_name: str = None
    avatar: str = None
    address: str = None
    website: str = None


class UserDtoOut(BaseModel):
    user_id: int

    class Config:
        orm_mode = True
