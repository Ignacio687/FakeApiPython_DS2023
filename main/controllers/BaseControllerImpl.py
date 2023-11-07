from main import router, app
from pydantic import BaseModel
from main.services import BaseServiceImpl, ProductServiceImpl
from main.controllers import BaseController
import json

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
            return json.dumps([object.to_dict() for object in service.findAll()])
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."+ str(e.args)}
    
    @router.get("/{id}")
    def getOne(id: int):
        try:
            return service.findById(id)
        except Exception as e:
            return {"error" : "Error. Por favor intente mas tarde."}
        
    @router.post("")
    def post(data: ProductModel):
        try:
            return json.dumps(service.save(data))
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