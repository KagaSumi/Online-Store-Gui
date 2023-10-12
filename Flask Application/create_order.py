import random

from app import app, db
from models import Order, Product, ProductsOrder

with app.app_context():
    o = Order(name="Tim", address="Vancouver")
    db.session.add(o)
    db.session.commit()

    print("New order, with ID", o.id)

    # Let's add five random products with random quantities to the order
    products = random.sample(Product.query.all(), k=5)

    for p in products:
        quantity = random.randint(1, 10)
        association = ProductsOrder(product=p, order=o, quantity=quantity)
        db.session.add(association)

    db.session.commit()
