from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# SQLALCHEMY_DATABASE_URL = "sqlite:///../database.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://cc85662_testdb:ueTprrn2@localhost:3306/cc85662_testdb"

# Online attemps
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://cc85662_testdb:ueTprrn2@5.23.50.27:3306/cc85662_testdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)



def get_db() -> Generator[Session, None, None]:
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()