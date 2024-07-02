from main.entities import BaseTable
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Producto(BaseTable):
    __tablename__ = "producto"

    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)
    category = Column(String)
    image = Column(String)
    count = Column(Integer, nullable=False)
    
    rating = relationship("Rating", back_populates="producto")

    def to_dict(self):
        return {
            "ID": self.id,
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "image": self.image,
            "count": self.count,
            "rating": [{
                "name": rating.name,
                "rate": rating.rate
            } for rating in self.rating]
        }
