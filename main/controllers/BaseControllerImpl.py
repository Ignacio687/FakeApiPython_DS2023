from main import router, app
from main.services import BaseServiceImpl, ProductServiceImpl
from main.controllers import BaseController
import json
from fastapi import Response
from main.customExceptions import ObjectNotFoundException
from abc import ABCMeta, abstractmethod

service = ProductServiceImpl()
headers = {"Content-Type": "application/json"}

class BaseControllerImplement(BaseController, metaclass=ABCMeta):
    
    @router.get("")
    def getAll():
        try:
            json_data = service.findAll()
            return Response(json_data, status_code=200, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
    
    @router.get("/{id}")
    def getOne(id: int):
        try:
            json_data = service.findById(id)
            return Response(json_data, status_code=200, headers=headers)
        except ObjectNotFoundException as e:
            json_data = json.dumps({"error" :str(e.args[0])})
            return Response(json_data, status_code=404, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
        
    @abstractmethod
    def post(self, object):
        pass

    @abstractmethod
    def put(self, object, id):
        pass

    @router.delete("/{id}")
    def delete(id: int):
        try:
            service.delete(id)
            return Response(None, status_code=204)
        except ObjectNotFoundException as e:
            json_data = json.dumps({"error" :str(e.args[0])})
            return Response(json_data, status_code=404, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)