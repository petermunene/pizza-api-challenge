# pizza-api-challenge
# 🍕 Pizza API

A simple Flask REST API for managing pizzas, restaurants, and their menu prices.

---

## ⚙️ Setup Instructions

1. **Clone the project**

```bash
git clone <repo-url>
cd pizza-api-challenge
Install dependencies using pipenv

bash
Copy
Edit
pipenv install
pipenv shell
Set environment variables & run Flask

bash
Copy
Edit
export FLASK_APP=server/app.py
flask run
🗃️ Database Migrations & Seeding
Initialize & migrate

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed data

bash
Copy
Edit
python server/seed.py
📮 API Routes Summary
Method	Route	Description
GET	/pizzas	Returns all pizzas
GET	/restaurants	Returns all restaurants
GET	/restaurants/<int:id>	Returns a specific restaurant & pizzas
DELETE	/restaurants/<int:id>	Deletes a restaurant & its associations
POST	/restaurant_pizzas	Adds a pizza to a restaurant

✅ Validation Rules
price must be between 1 and 30, else returns:

json
Copy
Edit
{ "errors": ["Price must be between 1 and 30"] }
🧪 Example Requests & Responses
GET /pizzas
json
Copy
Edit
[
  { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" },
  ...
]
GET /restaurants/1
json
Copy
Edit
{
  "id": 1,
  "name": "Mario's Pizza",
  "address": "123 Main St",
  "pizzas": [
    { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" },
    ...
  ]
}
POST /restaurant_pizzas
Request:

json
Copy
Edit
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2
}
Response:

json
Copy
Edit
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "address3"
  }
}
🔁 Postman Usage
Open Postman

Click Import

Upload: challenge-1-pizzas.postman_collection.json

Run all routes with sample data

