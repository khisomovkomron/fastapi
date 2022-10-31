from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router=auth.router)
app.include_router(router=todos.router)
