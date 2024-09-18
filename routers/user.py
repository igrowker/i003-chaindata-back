from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import EmailStr
from database.db_dependency import session
from services import user as service
from schemas import user as schema
from const import PATH_USERS, TAG_USERS

userRouter = APIRouter(
    prefix= PATH_USERS,
    tags=[TAG_USERS],
    responses={404: {"description": "Not found"}},
)

@userRouter.post("/add/", response_model=schema.UserResponse, status_code=201)
def create_user(request: schema.UserCreate, db:service.Session = Depends(session)) -> schema.UserResponse:
    """
    # Create new user
    """
    try:
        _user = service.insert_user(db, request)
        return _user
    except Exception as e:
        raise HTTPException(status_code=409, detail="the create gone wrong")
    
@userRouter.get("/", response_model=List[schema.UserResponse])
def get_all_users(db:service.Session = Depends(session)) -> List[schema.UserResponse]:
    """
    # Get a list of all users 
    """
    result = service.select_users(db)
    return result
    
@userRouter.get("/id/{user_id}", response_model=schema.UserResponse)  
def get_user_by_id(user_id:int, db:service.Session = Depends(session)) -> schema.UserResponse:
    """
    # Get a user by id
    """
    result = service.select_user_by_id(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"User with id:{user_id} not found")
    return result

@userRouter.get("/email/{email}", response_model=schema.UserResponse)  
def get_user_by_email(email:EmailStr, db:service.Session = Depends(session)) -> schema.UserResponse:
    """
    # Get a user by email
    """
    result = service.select_user_by_email(db, email)
    if not result:
        raise HTTPException(status_code=404, detail=f"User with email:{email} not found")
    return result

@userRouter.patch("/update/{user_id}", response_model=schema.UserResponse)
async def update_book(user_id:int, request: schema.UserUpdate, db:service.Session = Depends(session)) -> schema.UserResponse:
    """
    # Update a user by id
    """
    try:
        _user = service.update_user(db, user_id, request)
        return _user
    except Exception as e:
        raise HTTPException(status_code=404, detail="the updated gone wrong")

@userRouter.delete("/delete/{user_id}", response_model=schema.UserResponse)
async def delete_book(user_id:int, db:service.Session = Depends(session)) -> schema.UserResponse:
    """
    # Delete a user by id
    """
    try:
        _user = service.delete_book(db, user_id)
        return _user
    except Exception as e:
        raise HTTPException(status_code=404, detail="the deleted gone wrong")