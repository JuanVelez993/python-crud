from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import models

app=FastAPI()
db: List [models.User] =[  
    models.User(
        id=UUID("3e8e8500-ee67-446c-874d-149f9f3e746d"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=models.Gender.female,
        roles=[models.Role.user]
    ),
    models.User(
        id=UUID("27157124-bbb8-462e-bb0d-77d0ed21c984"),
        first_name="Karl",
        last_name="Jacobs",
        gender=models.Gender.male,
        roles=[models.Role.admin]
    )
]


@app.get('/')
async def root():
    return {"Hello": "world"}

@app.get('/api/v1/users')
async def fetch_users():
    return db;