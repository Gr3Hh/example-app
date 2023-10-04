from sqlalchemy.orm import Session

from models.users import User as UserModel
from schemas import users as user_schemas

from typing import Optional

from datetime import date


def user_birthday(db: Session, user_name: str) -> Optional[dict]:
    db_query_result = db.query(UserModel.dateOfBirth).filter(UserModel.name == user_name).first()
    result = None

    if db_query_result:
        remaining_days = days_till_birthday(db_query_result[0], date.today())
        if remaining_days == 0:
            result = {"message": f"Hello, {user_name}! Happy birthday!"}
        else:
            result = {"message": f"Hello, {user_name}! Your birthday is in {remaining_days} day(s)"}
    return result


def days_till_birthday(birthday: date, today: date) -> int:
    current_year = (date(today.year, birthday.month, birthday.day) - today).days
    if current_year >= 0:
        return current_year

    next_year = (date(today.year + 1, birthday.month, birthday.day) - today).days
    return next_year


def create_update_user(user_name: str, db: Session, user_data: user_schemas.UserCreateUpdate) -> None:
    if db.query(UserModel).where(UserModel.name == user_name).first():
        db.query(UserModel).where(UserModel.name == user_name).update({'dateOfBirth': user_data.dateOfBirth})
        db.commit()
    else:
        user = UserModel(name=user_name, dateOfBirth=user_data.dateOfBirth)
        db.add(user)
        db.commit()


def delete_user_from_db(db: Session, user_name: str) -> None:
    db.query(UserModel).filter(UserModel.name == user_name).delete()
    db.commit()
