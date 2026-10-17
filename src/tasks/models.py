from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from src.utils.dbConnection import Base

class TaskModel(Base):
    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    decription = Column(String)
    is_Completed= Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))