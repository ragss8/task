def userEntity(user) -> dict:
    return {
        'id':str(user["_id"]),
        'name':user["name"],
        'email':user["email"],
        'phone':user["phone"],
        'api_key':user["api_key"],
        'api_secret_key':user["api_secret_key"],
        'access_token':user["access_token"],
        'token_expiry_time':user["token_expiry_time"],
        'token_updated_at':user["token_updated_at"]
    }

def usersEntity(users) -> list:
    return [userEntity(user) for user in users]


def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]



