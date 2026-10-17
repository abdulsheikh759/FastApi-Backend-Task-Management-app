
from sqlalchemy import Column, Integer, String, INTEGER, Boolean, DATETIME
from src.utils.dbConnection import Base

class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobile_no = Column(String)

    