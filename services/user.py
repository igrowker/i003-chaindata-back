from pydantic import EmailStr
from typing import List
from sqlalchemy.orm import Session
from models.user import UserModel
from schemas import user as schema

def insert_user(db:Session, request:schema.UserCreate) -> schema.UserResponse:
    _validation = select_user_by_email(db, request.email)
    if _validation is not None:
        raise
    
    _user = UserModel(
        first_name = request.first_name,
        last_name = request.last_name,
        email = request.email,
        password = request.password
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

def select_users(db: Session) -> List[schema.UserResponse]:
    _users = db.query(UserModel).all()
    return _users


def select_user_by_id(db: Session, user_id: int) -> schema.UserResponse:
    _user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    return _user


def select_user_by_email(db: Session, mail: EmailStr) -> schema.UserResponse:
    _user = db.query(UserModel).filter(UserModel.email == mail).first()
    return _user


def update_user(db:Session, user_id:int, user:schema.UserUpdate) -> schema.UserResponse:
    _user = select_user_by_id(db, user_id)
    _user.first_name = user.first_name if user.first_name is not None else _user.first_name
    _user.last_name = user.last_name if user.last_name is not None else _user.last_name
    _user.password = user.password if user.password is not None else _user.password
    db.commit()
    db.refresh(_user)
    return _user

def delete_book(db:Session, user_id:int) -> schema.UserResponse:
    _user = select_user_by_id(db, user_id)
    db.delete(_user)
    db.commit()
    return _user
