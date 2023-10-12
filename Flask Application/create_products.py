from app import app, db
from models import Product

products = [
    ("apple", 1.49, 100),
    ("bananas", 3.49, 44),
    ("lemon", 1.0, 11),
    ("orange", 1.19, 40),
    ("raspberries", 7.99, 49),
    ("potato", 1.49, 67),
    ("onions", 3.99, 1),
    ("tomato", 2.99, 96),
    ("bread", 1.59, 13),
    ("chicken breast", 10.78, 26),
    ("chicken thigh", 8.99, 10),
    ("ground beef", 6.99, 39),
    ("cheese", 8.99, 45),
    ("milk", 3.49, 28),
    ("eggs", 4.49, 10),
]

with app.app_context():
    for product in products:
        obj = Product(name=product[0], price=product[1], quantity=product[2])
        db.session.add(obj)
        print(".", end="")
    print()
    db.session.commit()
