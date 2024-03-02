from . import db
from ..entities import Producto

class ProductRepo(Producto):
    
    def buscarPorPrecioMayorA(self, producto, precio_minimo: int):
        """ Buscar y filtrar por el campo price en la base de datos, buscando los productos cuyo precio sea mayor a 1000. """
        return db.query(producto).filter(producto.price > precio_minimo).all()

    def buscarPorPrecioEntre(self, producto, precio_minimo: int,precio_maximo: int):
        """ Buscar y filtrar por el campo price en la base de datos, buscando los productos cuyo precio sea entre 1000 y 2000. """
        return db.query(producto).filter(producto.price  > precio_minimo, producto.price < precio_maximo).all()
    