from uuid import UUID
from fastapi import APIRouter,HTTPException
from config.db import conn
from schemas.user import userEntity,usersEntity
from models.user import Gender,Role,User,UserUpdate

userRoutes=APIRouter()



@userRoutes.get('/api/v1/users')
async def fetch_users():
    return usersEntity(conn.userspython.users.find());
#in the url you can user /docs and /redoc to see the documentation with swagger
@userRoutes.post('/api/v1/users')
async def create_user(user:User):
    new_user=dict(user)
    id=conn.userspython.users.insert_one(new_user).inserted_id
    user=conn.userspython.users.find_one({"_id":id})
    return userEntity(user)
"""
@userRoutes.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        details=f'user with id {user_id} does not exist'
    )

@userRoutes.put('/api/v1/users/{user_id}')
async def update_user(user_id:UUID,user_update:UserUpdate):
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
    """