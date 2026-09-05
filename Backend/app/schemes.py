from pydantic import BaseModel,Field
class ProductCreate(BaseModel):
    name:str=Field(...,min_length=2,max_length=100)
    price:float=Field(...,gt=0)

class ProductResponse(BaseModel):
    id:int
    name:str
    price:float
    image: str | None = None

    class config:
        from_attributes=True

class UserCreate(BaseModel):
    username:str
    email:str
    password:str
class UserResponse(BaseModel):
    id:int
    username:str
    email:str

    class config:
        from_attributes=True
class UserLogin(BaseModel):
    email:str
    password:str

class CartItemCreate(BaseModel):
    product_id:int
    quantity:int=Field(...,gt=0)

class CartItemResponse(BaseModel):
    id:int
    cart_id:int
    product_id:int
    quantity:int

    class Config:
        from_attributes=True
