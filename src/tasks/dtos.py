from pydantic import BaseModel

class TaskSchema(BaseModel):
    title : str
    decription : str
    is_Completed : bool = False


class  TaskResponseSchema(BaseModel):
     id : int
     title: str
     decription : str
     is_Completed : bool
     user_id : int | None = 0