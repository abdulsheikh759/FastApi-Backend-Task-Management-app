
import email

from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name : str
    username: str
    password : str
    email : EmailStr
    mobile_no : str


class UserResponseModel(BaseModel):
    name : str
    username: str
    email : EmailStr
    mobile_no : str
    id : int


class LoginSchema(BaseModel):
    email : str
    password : str
