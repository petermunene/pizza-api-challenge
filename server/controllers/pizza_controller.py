from server.app import app,db
from server.models.pizza import Pizza

@app.route('/pizzas')
def get_pizzas():
    pizzas= db.session.query(Pizza).all()
    return [{'name':p.name,'ingredients':p.ingredients} for p in pizzas]

