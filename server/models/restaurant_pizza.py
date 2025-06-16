from server.app import db
from sqlalchemy import CheckConstraint
class RestaurantPizza(db.Model):
    __tablename__='restaurant_pizzas'
    id = db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer())
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurants.id',ondelete='CASCADE'))
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id',ondelete="CASCADE"))
    restaurant=db.relationship('Restaurant',back_populates="restaurant_pizzas")
    pizza=db.relationship('Pizza',back_populates="restaurant_pizzas")

    __table_args__=(
        CheckConstraint('price>1 AND price <30',name='check_price_range'),
    )