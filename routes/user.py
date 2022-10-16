from uuid import UUID
from fastapi import APIRouter,HTTPException,Response,status
from config.db import conn
from schemas.user import userEntity,usersEntity
from models.user import Gender,Role,User,UserUpdate
from starlette.status import HTTP_204_NO_CONTENT

userRoutes=APIRouter()



@userRoutes.get('/api/v1/users',response_model=list[User],tags=["users"])
async def fetch_users():
    return usersEntity(conn.userspython.users.find());
#in the url you can user /docs and /redoc to see the documentation with swagger
@userRoutes.post('/api/v1/users',response_model=User,tags=["users"])
async def create_user(user:User):
    new_user=dict(user)
    id=conn.userspython.users.insert_one(new_user).inserted_id
    user=conn.userspython.users.find_one({"_id":id})
    return userEntity(user)

@userRoutes.get('/api/v1/user/{user_id}',response_model=User,tags=["users"])
async def fetch_user(user_id:UUID):
    return userEntity(conn.userspython.users.find_one({"id":user_id}))


@userRoutes.delete('/api/v1/user/{user_id}',status_code=HTTP_204_NO_CONTENT,tags=["users"])
async def delete_user(user_id:UUID):
    userEntity(conn.userspython.users.find_one_and_delete({"id":user_id}))
    return Response(status_code=HTTP_204_NO_CONTENT)
    

@userRoutes.put('/api/v1/users/{user_id}',response_model=User,tags=["users"])
async def update_user(user_id:UUID,user_update:User):
    conn.userspython.users.find_one_and_update(
        {"id":user_id},{"$set":dict(user_update)})
    return userEntity(conn.userspython.users.find_one({"id":user_id}))
    