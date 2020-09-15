from fastapi import FastAPI
from src import settings
from fastapi_sqlalchemy import DBSessionMiddleware
from src.handlers.users import user_router

app = FastAPI()
app.include_router(user_router, prefix=settings.BASE_PATH)
app.add_middleware(DBSessionMiddleware, db_url=settings.SQLALCHEMY_DATABASE_URI)