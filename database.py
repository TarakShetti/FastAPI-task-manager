from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. DEFINE THE DATABASE URL
# We are using SQLite, which is just a file on your computer.
# "check_same_thread": False is needed only for SQLite.
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"

# 2. CREATE THE ENGINE
# The "engine" is the actual connection to the database.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. CREATE THE SESSION MAKER
# Each instance of the SessionLocal class will be a database session.
# Think of it as a "staging zone" for all the objects loaded into the
# database session object.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. CREATE THE BASE CLASS
# Later, we will inherit from this class to create each of our database models 
# (like User and Task).
Base = declarative_base()