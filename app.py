from flask import Flask, request

from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


items = {}

class Item(Resource):
    def get(self, name):
        return {"item": items.get(name, "Not found")}, 200 if name in items else 404

    def post(self):
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        items[name] = price
        return {"message": "Item added", "item": {name: price}}, 201

    def delete(self, name):
        if name in items:
            del items[name]
            return {"message": "Item deleted"}
        return {"message": "Item not found"}, 404

api.add_resource(Item, "/item", "/item/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
