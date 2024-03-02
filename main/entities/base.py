from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from main import Base

class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
