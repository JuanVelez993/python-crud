from typing import List
from fastapi import FastAPI
from routes.user import userRoutes
from docs import tags_metadata

app=FastAPI(
    title="REST API with FastAPI and MONGODB",
    description="a simple rest api to learn the basics of FastAPI",
    version="0.0.1",
    openapi_tags=tags_metadata
)
app.include_router(userRoutes)






    

