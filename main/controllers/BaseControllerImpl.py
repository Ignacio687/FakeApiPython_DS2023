from main import router, app
from pydantic import BaseModel
from main.services import BaseServiceImpl, ProductServiceImpl
from main.controllers import BaseController
import json
from fastapi import Response

service = ProductServiceImpl()
class RatingModel(BaseModel):
    rate: int
    count: int

class ProductModel(BaseModel):
    title: str
    price: int
    description: str
    category: str
    image: str
    rating: RatingModel

class BaseControllerImplement(BaseController):

    @router.get("")
    def getAll():
        try:
            headers = {
                "Content-Type": "application/json"
            }
            json_data = json.dumps([object.to_dict() for object in service.findAll()])
            return Response(json_data, status_code=200, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
    
    @router.get("/{id}")
    def getOne(id: int):
        try:
            return service.findById(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
        
    @router.post("")
    def post(data: ProductModel):
        try:
            headers = {
                    "Content-Type": "application/json"
                }
            json_data = service.save(data)
            #json_data = json.dumps(rrt)
            return Response(json_data, status_code=201, headers=headers)
        except Exception as e:
            print(e.args)
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.put("/{id}", response_model=BaseModel)
    def put(base: BaseModel, id: int):
        try:
            return service.update(base, id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}

    @router.delete("/{id}")
    def delete(id: int):
        try:
            return service.delete(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}