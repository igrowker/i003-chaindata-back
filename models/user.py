from database.session import Base
from sqlalchemy import Column, String, Integer, Boolean

class UserModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=30))
    last_name = Column(String(length=30))
    email = Column(String(length=100))
    password = Column(String(length=250))