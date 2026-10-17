from fastapi import Depends, Request, status, HTTPException
from src.utils.settings import setting
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from src.user.model import UserModel
from src.utils.dbConnection import get_db



def is_Authenticated(request:Request, db:Session = Depends(get_db) ):
    try:
        token = request.headers.get("authorization")
        if not token:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorized")
      
        token = token.split(" ")[-1]

        data = jwt.decode(token, setting.SECRET_KEY, setting.ALGORITHM )
        user_id = data.get("_id")
        # exp_time = data.get("exp")

        # current_time = datetime.now().timestamp()


        # if current_time > exp_time:
        #   raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorized")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user not match")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorized")