from typing import Union
from fastapi import FastAPI # type: ignore
from src.config.db_config import create_db_and_tables
from src.modules.user.model import create_user_table
from src.modules.user.router import user_router

app = FastAPI()


# Create the database and tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_user_table()
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Register the routers
app.include_router(user_router, prefix="/api/v1/user", tags=["User"])
