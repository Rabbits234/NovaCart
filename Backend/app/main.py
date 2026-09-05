from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database import get_db,engine
from fastapi import Depends
from app.crud import (get_products,create_product,get_product_by_id,delete_product,update_product,create_user,get_user_by_email,get_user_cart,add_to_cart,create_cart)
from app.schemes import ProductCreate,ProductResponse,UserCreate,UserResponse,UserLogin,CartItemCreate,CartItemResponse
from app.models import Base,Product,User,Cart,CartItem
from app.auth import verify_password,create_access_token
from app.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{"message":"  Welcome to NovaCart"}

@app.get("/products", response_model=list[ProductResponse])
def read_products(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_products(db)

@app.post("/products",response_model=ProductResponse)
def add_product(product: ProductCreate,db:Session=Depends(get_db)):
    return create_product(db,product)

@app.get("/products/{product_id}",response_model=ProductResponse)
def read_product(product_id:int,db:Session=Depends(get_db)):
    product=get_product_by_id(db,product_id)

    if product is None:
        return{"error":"Product not found"}
    else:
        return product

@app.delete("/products/{product_id}")
def remove_product(product_id:int,db:Session=Depends(get_db)):
    product=delete_product(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product is not found")
    return{"message":"Product successfully deleted"}

@app.put("/products/{product_id}",response_model=ProductResponse)
def edit_product(product_id:int,product:ProductCreate,db:Session=Depends(get_db)):
    updated_product=update_product(db,product_id,product)
    if updated_product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    
    return updated_product
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.post("/login")
def login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    db_user=get_user_by_email(db,user.username)

    if db_user is None:
        raise HTTPException(status_code=401,detail="Invalid password or email")
    
    if not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=401,detail="Invalid password or email")
    
    token = create_access_token(
    data={"sub": db_user.email}
    )

    return {
    "access_token": token,
    "token_type": "bearer"
    }

@app.post("/cart/items",response_model=CartItemResponse)
def add_cart_item(item:CartItemCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    user_email=current_user["sub"]

    db_user=get_user_by_email(db,user_email)

    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    
    cart=get_user_cart(db,db_user.id)

    if cart is None:
        cart=create_cart(db,db_user.id)

    return add_to_cart( db,cart.id,item.product_id,item.quantity)

@app.get("/cart")
def get_cart(db:Session=Depends(get_db),current_user=Depends(get_current_user)):

    db_user=get_user_by_email(db,current_user["sub"])

    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    
    cart=get_user_cart(db,db_user.id)

    if cart is None:
        raise HTTPException(status_code=404,detail="Cart not found")
    
    return cart