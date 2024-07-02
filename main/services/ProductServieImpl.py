from main import db
from . import ProductService, BaseServiceImpl
from ..respositories import ProductRepo
from main.entities import Producto, Rating
import json

class ProductServiceImpl(BaseServiceImpl):
    def __init__(self):
        self.repository = ProductRepo()
        self.entity = Producto
    
    def buscarPorPrecioMayorA(self, precioMinimo) -> list|Exception:
        return json.dumps([producto.to_dict() for producto in self.repository
                          .buscarPorPrecioMayorA(self.entity, precioMinimo)])
    
    def buscarPorPrecioEntre(self, precioMinimo, precioMaximo) -> list|Exception:
        return json.dumps([producto.to_dict() for producto in self.repository
                          .buscarPorPrecioEntre(self.entity, precioMinimo, precioMaximo)])

    def save(self, data) -> list|Exception:
        producto_data = data.model_dump()
        rating_data = producto_data.pop("rating")
        producto = Producto(**producto_data)
        rating = Rating(**rating_data, producto=producto)
        producto.rating = [rating]
        db.add(producto)
        db.add(rating)
        db.commit()
        return json.dumps(producto.to_dict())
        
    def update(self, entity, id) -> list|Exception:
        newproducto = entity.model_dump()
        newRating = newproducto.pop("rating")
        producto = db.query(self.entity).filter_by(id=id).first()
        if producto is None:
            self.save(entity)
        else:
            for key, value in newproducto.items():
                setattr(producto, key.lower(), value)
            rating = Rating(**newRating, producto=producto)
            producto.rating = [rating]
            db.add(producto)
            db.add(rating)
            db.commit()
            return json.dumps(producto.to_dict())