from main import db
from . import ProductService, BaseServiceImpl
from ..respositories import ProductRepo
from main.entities import Producto, Rating

class ProductServiceImpl(BaseServiceImpl):
    def __init__(self):
        self.repository = ProductRepo()
        self.entity = Producto
    
    def buscarPorPrecioMayorA(self, precioMinimo) -> list|Exception:
        try:
            return self.repository.buscarPorPrecioMayorA(self.entityProducto, precioMinimo)
        except Exception as e:
            raise Exception(str(e))

    def buscarPorPrecioEntre(self, precioMinimo, precioMaximo) -> list|Exception:
        try:
            return self.repository.buscarPorPrecioEntre(self.entityProducto, precioMinimo, precioMaximo)
        except Exception as e:
            raise Exception(str(e))

    def save(self, data):
        try:
            producto_data = data.model_dump()
            rating_data = producto_data.pop("rating")
            producto = Producto(**producto_data)
            rating = Rating(**rating_data, producto=producto)
            producto.rating = [rating]
            producto = db.add(producto)
            db.add(rating)
            db.commit()
            return producto
        except Exception as e:
            raise Exception(str(e))