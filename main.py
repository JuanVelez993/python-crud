from typing import List
from uuid import UUID
from fastapi import FastAPI,HTTPException
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
#in the url you can user /doc and /redoc to see the documentation with swagger
@app.post('/api/v1/users')
async def create_user(user:models.User):
    db.append(user)
    return {'id': user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        details=f'user with id {user_id} does not exist'
    )

@app.put('/api/v1/users/{user_id}')
async def update_user(user_id:UUID,user_update:models.UserUpdate):
    for user in db:
        if user.id==user_id:
            if user_update. first_name is not None:
                user.first_name = user_update.first_name
            if user_update. last_name is not None:
                user.last_name = user_update.last_name
            if user_update. middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update. roles is not None:
                user. roles = user_update. roles
            return
    raise HTTPException(
        status_code=404,
        details=f'user with id {user_id} does not exist'
    )


    

