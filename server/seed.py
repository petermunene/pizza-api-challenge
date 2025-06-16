import sys
import os

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza


# Run this inside the Flask app context
with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Side St")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Pineapple, Ham")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    # Create restaurant-pizza associations
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
