from sqlalchemy import Column,Integer,Numeric,String,ForeignKey
from sqlalchemy.orm import declarative_base

Base=declarative_base()
class Product(Base):
    __tablename__ = "products"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    price=Column(Numeric,nullable=False)
    image = Column(String, nullable=True)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)

class Cart(Base):
    __tablename__="carts"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)


class CartItem(Base):
    __tablename__="cart_items"

    id=Column(Integer,primary_key=True,index=True)
    cart_id=Column(Integer,ForeignKey("carts.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    quantity=Column(Integer,nullable=False)

