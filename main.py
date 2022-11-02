from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos, users, address
from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory='static'), name='static')

app.include_router(router=auth.router)
app.include_router(router=todos.router)
app.include_router(router=users.router)
app.include_router(router=address.router)
