from app import db

class Customer(db.Model):
    id       = db.Column(db.Integer, primary_key=True, unique = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email    = db.Column(db.String(120), index=True, unique=True)
    orders   = db.relationship('Orders', backref = "Customer", lazy = "dynamic")

    def __repr__(self):
        return '<Customer {}'.format(self.username)

class Orders(db.Model):
    order_id    = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String(64), index=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Order {}'.format(self.description)