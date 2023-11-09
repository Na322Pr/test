from fastapi import FastAPI, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import SignUpDto, UserDto

app = FastAPI()

@app.post("/sign-up", response_model=int)
async def sign_up(sign_up_request: SignUpDto, db: Session = Depends(get_db)) -> int:
    user = User(**sign_up_request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.id


@app.get("/{user_id}", response_model=UserDto | None)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> UserDto | None:
    query = select(User).where(User.id == user_id).limit(1)
    user = db.execute(query).scalar()
    return user


@app.get("/", response_model=list[UserDto])
async def get_users(offset: int = Query(0), limit: int = Query(10), db: Session = Depends(get_db)) -> list[UserDto]:
    query = select(User).offset(offset).limit(limit)
    users = db.execute(query).scalars()
    return users