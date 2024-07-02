from main import db
from . import BaseService
from main.respositories import BaseRepo
from sqlalchemy.orm import Session
from main.entities import BaseTable
from main.customExceptions import ObjectNotFoundException
import json
from abc import ABCMeta, abstractmethod

class BaseServiceImpl(BaseService, metaclass=ABCMeta):
    def __init__(self):
        self.repository = BaseRepo()
        self.entity = BaseTable

    def findAll(self) -> list|Exception:
        objects = db.query(self.entity).all()
        objects = json.dumps([object.to_dict() for object in objects])
        return objects

    def findById(self, id) -> list|Exception:
        object = db.query(self.entity).filter_by(id=id).first()
        if object is None:
            raise ObjectNotFoundException(str("El objeto con id: %d no existe" % (id)))
        object = json.dumps(object.to_dict())
        return object

    @abstractmethod
    def save(self, entity) -> list|Exception:
        pass

    @abstractmethod
    def update(self, entity, id) -> list|Exception:
        pass

    def delete(self, id) -> list|Exception:
        object = db.query(self.entity).filter_by(id=id).first()
        if object is not None:
            db.delete(object)
            db.commit()
            return True
        else:
            raise ObjectNotFoundException(str("El objeto con id: %d no existe" % (id)))