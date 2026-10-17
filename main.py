from fastapi import FastAPI
from src.utils.dbConnection import Base, engine
from src.tasks.router import tasks_route
# from src.tasks.models import TaskModel
from src.user.router import user_routes

Base.metadata.create_all(engine)
app = FastAPI(title="this is my task management application")
app.include_router(tasks_route)
app.include_router(user_routes)