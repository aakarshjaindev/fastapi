from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: Optional[bool] = True

class UserRespon