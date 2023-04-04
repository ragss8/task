from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str 
    email: EmailStr
    phone: str 
    api_key: str 
    api_secret_key: str 
    access_token:str 
    token_expiry_time:datetime
    token_updated_at:datetime
