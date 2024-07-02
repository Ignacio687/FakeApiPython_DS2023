from main import router, app
from pydantic import BaseModel
from main.services import ProductServiceImpl
from main.controllers import BaseControllerImplement
from fastapi import Response
import json

urlPrefix: str="/fakestoreapi.com/products"
service = ProductServiceImpl()
headers = {"Content-Type": "application/json"}

class RatingModel(BaseModel):
    name: str
    rate: int

class ProductModel(BaseModel):
    title: str
    price: int
    description: str
    category: str
    image: str
    count: int
    rating: RatingModel

class ProductController(BaseControllerImplement):

    @router.get("/precio/{precioMinimo}")
    def get_all(precioMinimo: int):
        try:
            json_data = service.buscarPorPrecioMayorA(precioMinimo)
            return Response(json_data, status_code=200, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
    
    @router.get("/precio/{precioMinimo}/{precioMaximo}")
    def get_one(precioMinimo: int, precioMaximo: int):
        try:
            json_data = service.buscarPorPrecioEntre(precioMinimo, precioMaximo)
            return Response(json_data, status_code=200, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
        
    @router.post("")
    def post(data: ProductModel):
        try:
            json_data = service.save(data)
            return Response(json_data, status_code=201, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)

    @router.put("/{id}", response_model=ProductModel)
    def put(data: ProductModel, id: int):
        try:
            json_data = service.update(data, id)
            return Response(json_data, status_code=200, headers=headers)
        except Exception as e:
            json_data = json.dumps({"error" : "Error. Por favor intente mas tarde."+ str(e.args)})
            return Response(json_data, status_code=500, headers=headers)
        
app.include_router(router, prefix=urlPrefix)