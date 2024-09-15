from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

connectionString = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# use echo=True for debugging
engine = create_engine(connectionString, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()