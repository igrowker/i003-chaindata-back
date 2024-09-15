from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import EmailStr
from database.db_dependency import session
from services import user
from schemas.user import UserResponse, UserRequest
from const import PATH_USERS, TAG_USERS

userRouter = APIRouter(
    prefix= PATH_USERS,
    tags=[TAG_USERS],
    responses={404: {"description": "Not found"}},
)

@userRouter.post("/add/", response_model=UserResponse, status_code=201)
def create_user(request: UserRequest, db:user.Session = Depends(session)) -> UserResponse:
    """
    # Create new user
    """
    validation = user.select_user_by_email(db, request.email)
    if validation is not None:
        raise HTTPException(status_code=404, detail=f"User with email:{request.email} already exists")
    result = user.insert_user(db, request)
    return result

@userRouter.get("/", response_model=List[UserResponse])
def get_all_users(db:user.Session = Depends(session)) -> List[UserResponse]:
    """
    # Get a list of all users 
    """
    result = user.select_users(db)
    return result
    
@userRouter.get("/id/{user_id}", response_model=UserResponse)  
def get_user_by_id(user_id:int, db:user.Session = Depends(session)) -> UserResponse:
    """
    # Get a user by id
    """
    result = user.select_user_by_id(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"User with id:{user_id} not found")
    return result

@userRouter.get("/email/{email}", response_model=UserResponse)  
def get_user_by_email(email:EmailStr, db:user.Session = Depends(session)) -> UserResponse:
    """
    # Get a user by email
    """
    result = user.select_user_by_email(db, email)
    if not result:
        raise HTTPException(status_code=404, detail=f"User with email:{email} not found")
    return result

@userRouter.patch("/update/{user_id}")
async def update_book(user_id:int, request: UserRequest, db:user.Session = Depends(session)):
    """
    # Update a user by id
    """
    try:
        _user = user.update_user(db, user_id, request)
        return _user
    except Exception as e:
        return HTTPException(status_code=304, detail="the updated gone wrong")

@userRouter.delete("/delete/{user_id}")
async def delete_book(user_id:int, db:user.Session = Depends(session)):
    """
    # Delete a user by id
    """
    try:
        _user = user.delete_book(db, user_id)
        return _user
    except Exception as e:
        return HTTPException(status_code=304, detail="the deleted gone wrong")