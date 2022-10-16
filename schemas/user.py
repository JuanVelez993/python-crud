def userEntity(item) -> dict:
    return{
        "id": item["id"],
        "first_name": item[ "first_name"],
        "last_name": item["last_name"],
        "middle_name": item["middle_name"],
        "gender": item["gender"],
        "roles": item["roles"]
        
    }

def usersEntity (entity) -> list:
    return [userEntity(item) for item in entity]

    
    
    