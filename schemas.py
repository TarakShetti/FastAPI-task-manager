from pydantic import BaseModel
from typing import List, Optional

# --- TASK SCHEMAS ---

# Shared properties (used for creating and reading)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Properties to receive on task creation
class TaskCreate(TaskBase):
    pass

# Properties to return to client (includes ID and user_id)
class Task(TaskBase):
    id: int
    user_id: int

    # This tells Pydantic to read data even if it's not a dict, but an ORM model
    class Config:
        from_attributes = True 

# --- USER SCHEMAS ---

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int
    is_active: bool = True
    tasks: List[Task] = []

    class Config:
        from_attributes = True