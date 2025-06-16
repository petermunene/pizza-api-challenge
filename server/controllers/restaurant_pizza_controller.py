from server.app import app,db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza   
from flask import request
@app.route('/restaurant_pizzas',methods=['POST'])
def post_restaurant_pizza():
    data=request.get_json()
    price=int(data.get('price'))
    pizza_id=int(data.get('pizza_id'))
    restaurant_id=int(data.get('restaurant_id'))

    if not (1<=price<=30):
        return { "errors": ["Price must be between 1 and 30"] },400
    r=db.session.query(Restaurant).filter(Restaurant.id==restaurant_id).first()
    p= db.session.query(Pizza).filter(Pizza.id=pizza_id).first()

    rp=RestaurantPizza(price=price,pizza_id=pizza_id,restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return { 
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id, 
        "restaurant_id": rp.restaurant_id, 
        "pizza": { "id": p.id, "name": p.name, "ingredients":p.ingredients },
        "restaurant": { "id": r.id, "name": r.name, "address": r.address }
         }
    

