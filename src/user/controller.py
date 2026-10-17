
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks, HTTPException, status, Request
from src.user.model import UserModel
from src.utils.settings import setting
from datetime import datetime, timedelta
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.mail import send_email


password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


async def ragister(body:UserSchema, db:Session, bg_task:BackgroundTasks):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="username already exiting")
    
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail="email already exiting")


    # hasing password
    hash_password = get_password_hash(body.password)
    new_user = UserModel(
        name = body.name,
        username = body.username,
        email = body.email,
        mobile_no = body.mobile_no,
        password = hash_password

    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # send mail by user confirmation
    # res = await send_email([new_user.email])
    bg_task.add_task(send_email, [new_user.email])
    # print(res)


    return new_user


def login_user(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="email not match")

    if not verify_password(body.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password not match")


    exp_time = datetime.now() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({"_id": user.id, "username":user.username, "exp":exp_time.timestamp()}, setting.SECRET_KEY, setting.ALGORITHM)
    
    return {"message":"login successfully...","token":token}



