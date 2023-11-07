from main import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)
    category = Column(String)
    image = Column(String)
    
    rating = relationship("Rating", back_populates="producto")

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "description": self.description,
            "category": self.category,
            "image": self.image,
            "rating": {
                "rate": self.rating[0].rate,  # Suponiendo que solo hay un Rating por Producto
                "count": self.rating[0].count  # Suponiendo que solo hay un Rating por Producto
            }
        }
