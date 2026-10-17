from fastapi import APIRouter, Depends, Request, status, BackgroundTasks
from sqlalchemy.orm import Session
from src.user.dtos import UserSchema, UserResponseModel, LoginSchema
from src.utils.dbConnection import get_db
from src.user import controller

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
async def register(body:UserSchema, bg_task:BackgroundTasks, db:Session = Depends(get_db)):
    return await controller.ragister(body, db, bg_task)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body:LoginSchema, db:Session = Depends(get_db)):
    return controller.login_user(body, db) 

@user_routes.get("/is_auth", status_code=status.HTTP_200_OK, response_model=UserResponseModel)
def is_Auth(request:Request, db:Session = Depends(get_db)):
    return controller.is_Authenticated(request, db)