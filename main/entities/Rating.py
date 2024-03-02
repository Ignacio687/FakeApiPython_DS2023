from main.entities import BaseTable
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, DeclarativeBase

class Rating(BaseTable):
    __tablename__ = "rating"

    name = Column(String, nullable=False)
    rate = Column(Integer, nullable=False)

    producto_id = Column(Integer, ForeignKey("producto.id"))
    producto = relationship("Producto", back_populates="rating")