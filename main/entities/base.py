from main import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class BaseTable(Base):
    __tablename__ = "base"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
