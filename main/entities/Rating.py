from main import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rate = Column(Integer, nullable=False)
    count = Column(Integer)

    producto_id = Column(Integer, ForeignKey("producto.id"))
    producto = relationship("Producto", back_populates="rating")