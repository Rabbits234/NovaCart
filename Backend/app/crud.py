from app.models import Product,User,Cart,CartItem
from app.auth import hash_password
def get_products(db):
    return db.query(Product).all()
def create_product(db,product):
    new_product=Product(
        name=product.name,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
def get_product_by_id(db,product_id):
    return db.query(Product).filter(Product.id==product_id).first()

def delete_product(db,product_id):
    product=db.query(Product).filter(Product.id==product_id).first()
    if product is None:
        return None
    db.delete(product)
    db.commit()
    return product
def update_product(db,product_id,product):
    existing_product=db.query(Product).filter(Product.id==product_id).first()
    if existing_product is None:
        return None
    existing_product.name=product.name
    existing_product.price=product.price
    db.commit()
    db.refresh(existing_product)
    return existing_product
def create_user(db, user):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
def get_user_by_email(db,email):
    return db.query(User).filter(User.email==email).first()

def get_user_cart(db,user_id):
    return db.query(Cart).filter(Cart.user_id==user_id).first()

def get_cart_with_items(db, user_id):
    cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if cart is None:
        return None

    items = db.query(CartItem).filter(CartItem.cart_id == cart.id).all()

    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "items": items
    }

def create_cart(db,user_id):
    cart=Cart(user_id=user_id)

    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart

def add_to_cart(db,cart_id,product_id,quantity):
    item=CartItem(cart_id=cart_id,product_id=product_id,quantity=quantity)

    db.add(item)
    db.commit()
    db.refresh(item)

    return item

