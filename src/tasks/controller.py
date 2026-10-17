from fastapi import HTTPException
from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.user.model import UserModel

def create_task(body : TaskSchema, db:Session, user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(title = data["title"], decription = data["decription"], is_Completed = data["is_Completed"],
    user_id = user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # return {"status":"Task created succesfully...", "data":new_task}
    return new_task


def get_all_tasks(db:Session, user: UserModel):
    # tasks = db.query(TaskModel).all()
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    # return {"status":"All Tasks ", 'data':tasks}
    return tasks

def get_id_task(task_id:int, db:Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail='Task id not correct')

    # return {"status":"get task", "data":task}
    return task


def update_task(body: TaskSchema, task_id:int, db:Session, user:UserModel):
    task:TaskModel = db.query(TaskModel).get(task_id)
    if not task:
         raise HTTPException(404, detail='data not find')

    if task.user_id != user.id:
         raise HTTPException(401, detail='data not find')


    # task.title = body.title
    # task.decription = body.decription
    # task.is_Completed = body.is_Completed

    body = body.model_dump()
    for field, value in body.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    # return {"status":"task updateed successfully", "data":task}
    return task


def delete_task(task_id:int, db:Session, user:UserModel):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail='data not find')

    if task.user_id != user.id:
        raise HTTPException(401, detail='data not find')

    db.delete(task)
    db.commit()

    # return {"status":"task is deleted"}
    return None