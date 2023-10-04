from pydantic import PastDate, BaseModel


class UserBase(BaseModel):
    pass


class UserResponse(BaseModel):
    message: str


class UserCreateUpdate(BaseModel):
    dateOfBirth: PastDate
