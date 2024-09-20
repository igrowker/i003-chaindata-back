from database.session import Base
from sqlalchemy import Column, String, Integer, Boolean, JSON

class UserModel(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, length=30)
    last_name = Column(String, length=30)
    email = Column(String, length=100)
    password = Column(String, length=250)

class DemandPrediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    product = Column(Integer, nullable=False)
    historical_demand = Column(JSON)
    date_prediction = Column(JSON)
    demand_prediction = Column(JSON)