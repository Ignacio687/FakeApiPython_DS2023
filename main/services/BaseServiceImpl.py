from main import db
from . import BaseService
from main.respositories import BaseRepo
from sqlalchemy.orm import Session
from main.entities import BaseTable

class BaseServiceImpl(BaseService):
    def __init__(self):
        self.repository = BaseRepo()
        self.entity = BaseTable

    def findAll(self):
        try:
            productos = db.query(self.entity).all()
            return productos
        except Exception as e:
            raise Exception(str(e))

    def findById(self, id):
        try:
            producto = db.query(self.entity).filter_by(id=id).first()
            return producto
        except Exception as e:
            raise Exception(str(e))

    def save(self, data):
        pass

    def update(self, id):
        try:
            db.merge(self.entity)
            db.commit()
            return self.entity
        except Exception as e:
            raise Exception(str(e))

    def delete(self, id):
        try:
            producto = db.query(self.entity).filter_by(id=id).first()
            if producto:
                db.delete(producto)
                db.commit()
                return True
            else:
                raise Exception()
        except Exception as e:
            raise Exception(str(e))