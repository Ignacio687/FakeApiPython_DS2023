from fastapi import FastAPI, APIRouter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.openapi.utils import get_openapi

app = FastAPI()

router = APIRouter()

# Configura la base de datos SQLite
DATABASE_URL = "sqlite:///fakeApi.db"
engine = create_engine(DATABASE_URL)

# Crea una sesión SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Define una tabla de ejemplo usando SQLAlchemy
Base = declarative_base()
