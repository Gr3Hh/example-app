from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import users
from controllers.users import user_birthday, create_update_user, delete_user_from_db
from core.db import get_db


router = APIRouter()


@router.get("/{user_name}", response_model=users.UserResponse)
def get_user_birthday(user_name: str, db: Session = Depends(get_db)) -> dict:
    result_birthday = user_birthday(db, user_name=user_name)
    if result_birthday is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result_birthday


@router.put("/{user_name}", status_code=204)
def update_create_user(user_name: str, user_data: users.UserCreateUpdate, db: Session = Depends(get_db)) -> None:
    if not user_name.isalpha():
        raise HTTPException(status_code=400, detail='name must contain only letters')
    create_update_user(db=db, user_name=user_name, user_data=user_data)


@router.delete("/{user_name}")
def delete_user(user_name: str, db: Session = Depends(get_db)) -> None:
    delete_user_from_db(db, user_name=user_name)
