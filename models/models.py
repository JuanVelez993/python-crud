

from enum import Enum
from typing import Optional,List
from uuid import uuid4,UUID

from pydantic import BaseModel

class Gender (str, Enum) :
    male = "male"
    female ="female"

class Role (str, Enum) :
    admin = "admin"
    user ="user"

class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str]
    gender:Gender
    roles:List[Role]

class UserUpdate(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:Optional[str]
    last_name:Optional[str]
    middle_name:Optional[str]
    gender:Optional[Gender]
    roles:List[Role]