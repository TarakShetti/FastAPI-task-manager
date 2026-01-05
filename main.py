from fastapi import FastAPI
from . import models, database
from .routes import users, tasks

# 1. CREATE DATABASE TABLES
# This line checks your 'models.py' file and creates the actual tables 
# in the SQLite database if they don't exist yet.
models.Base.metadata.create_all(bind=database.engine)

# 2. INITIALIZE APP
app = FastAPI(
    title="Task Manager API",
    description="A simple task manager with JWT Auth",
    version="1.0.0"
)

# 3. INCLUDE ROUTERS
# This connects the "users.py" and "tasks.py" files to the main app.
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API"}