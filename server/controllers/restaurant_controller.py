from server.app import app,db
from server.models.restaurant import Restaurant

@app.route('/restaurants')
def get():
    restaurants= db.session.query(Restaurant).all()
    return [{'name':r.name} for r in restaurants]
@app.route('/restaurants/<int:id>',methods=['GET'])
def get_by_id(id):
    r=db.session.query(Restaurant).filter(Restaurant.id==id).first()
    if r :
        return {
            'id':r.id,
            'name':r.name,
            'address':r.address
            }
    else :
        return {
           "error": "Restaurant not found"  
        },404
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    r=db.session.query(Restaurant).filter(Restaurant.id==id).first()
    if r :
        db.session.delete(r)
        db.session.commit()
        return '',204
    else:
        return { "error": "Restaurant not found" },404

 