from typing import List
from uuid import UUID
from fastapi import FastAPI
from models.user import Gender,Role,User
from routes.user import userRoutes

app=FastAPI()
app.include_router(userRoutes)






    

