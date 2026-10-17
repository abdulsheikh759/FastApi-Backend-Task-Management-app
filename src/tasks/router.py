from fastapi import APIRouter, Depends, status
from  src.utils.dbConnection import get_db
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from typing import List
from src.utils.helper import is_Authenticated
from src.user.model import UserModel

tasks_route = APIRouter(prefix="/tasks")

@tasks_route.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db = Depends(get_db), user:UserModel = Depends(is_Authenticated)):
    return controller.create_task(body, db, user)

@tasks_route.get("/all_tasks", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db = Depends(get_db), user:UserModel = Depends(is_Authenticated)):
    return controller.get_all_tasks(db, user)

@tasks_route.get('/task/{task_id}', response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_id_task(task_id:int, db = Depends(get_db), user:UserModel = Depends(is_Authenticated)):
    return controller.get_id_task(task_id, db)

@tasks_route.put('/update/{task_id}', response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema, task_id:int, db= Depends(get_db), user:UserModel = Depends(is_Authenticated)):
    return controller.update_task(body, task_id, db, user)

@tasks_route.delete("/delete/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db=Depends(get_db), user:UserModel = Depends(is_Authenticated)):
    return controller.delete_task(task_id, db, user)