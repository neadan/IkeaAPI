from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product:
    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'name': self.name,
            'year': self.year,
            'price': self.price
        }


class Sink(db.Model, Product):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)


class Lamp(db.Model, Product):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)

