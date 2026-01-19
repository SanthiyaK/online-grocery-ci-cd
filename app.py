from flask import Flask, jsonify

app = Flask(__name__)

grocery_items = [
    {"id": 1, "name": "Rice", "price": 50},
    {"id": 2, "name": "Milk", "price": 30},
    {"id": 3, "name": "Sugar", "price": 40}
]

@app.route("/")
def home():
    return "Welcome to Online Grocery Store"

@app.route("/items")
def items():
    return jsonify(grocery_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
