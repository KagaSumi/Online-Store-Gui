from database import db
from datetime import datetime


class Product(db.Model):
    """This class represents a product in a store.
    It contains information describing the product
    Name : Name of the product
    Price : Price of the product
    Quantity : Quantity of the product
    """
    name = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}

    def process(self, value: int) -> int:
        """This function is called when we are processing the order.
        This will return the value of what the order's product quantity should be set as.
        While subtracting the order's quantity from our stock.

        Args:
            value (int): How much the order is requesting from

        Returns:
            int: Update quantity of the order
        """
        if value > self.quantity:
            value = self.quantity
            self.quantity = 0
            return value
        self.quantity -= value
        return value


class Order(db.Model):
    """This represents a single order for products at a store
    It contains the name of a id,name,address,completed, and products

    Name : Is the name of the one who placed the order
    Address : Is the address of the orderer
    Completed : Stores a boolean indicating whether the order has been completed
    Product : Is a list containing dictionaries containing the name of the product 
    with the quantity of the product in respect of the order 
    """
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String)
    address = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    time_processed = db.Column(db.DateTime)
    products = db.relationship('ProductsOrder',cascade="all,delete", back_populates='order')
    
    def to_dict(self):
        new_dict = {}
        total = 0
        new_dict['id'] = self.id
        new_dict['customer_name'] = self.name
        new_dict['customer_address'] = self.address
        new_dict["products"] = []
        for product in self.products:
            total += db.session.get(Product,
                                    product.product_name).price * product.quantity
            new_dict['products'].append(
                {"name": product.product_name, "quantity": product.quantity})
        new_dict['total'] = round(total, 2)
        new_dict['completed'] = self.completed
        new_dict['time_created'] = self.time_created
        new_dict['time_processed'] = self.time_processed
        return new_dict


class ProductsOrder(db.Model):
    # Product foreign key is name
    product_name = db.Column(db.ForeignKey("product.name"), primary_key=True)
    # Order foreign key is ID
    order_id = db.Column(db.ForeignKey("order.id"), primary_key=True)
    # This is how many items we want
    quantity = db.Column(db.Integer, nullable=False)
    # Relationships and backreferences for SQL Alchemy
    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='products')
