from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world!"


products = [
    {
        "id": 1,
        "name": "Tea",
        "price": 1.2,
        "imageUrl": "https://www.twinings.co.uk/app_/responsive/TwiningsUKI/media/content/About-Tea/shutterstock_126275183.jpg?w=1260",
    },
    {
        "id": 2,
        "name": "Coffee",
        "price": 3.5,
        "imageUrl": "https://media3.s-nbcnews.com/j/newscms/2019_33/2203981/171026-better-coffee-boost-se-329p_67dfb6820f7d3898b5486975903c2e51.fit-1240w.jpg",
    },
    {
        "id": 3,
        "name": "Beer",
        "price": 2.5,
        "imageUrl": "https://i.pinimg.com/736x/9b/da/95/9bda953d4702d936c398249e0898bafc.jpg",
    },
    {
        "id": 4,
        "name": "Wine",
        "price": 4.5,
        "imageUrl": "data:image/jpeg;base64,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",
    },
]


@app.route("/product")
def get_products():
    return json.dumps(products)


tea_ingredients = [
    {"name": "Water", "content": 90, "isCommonAllergen": False},
    {"name": "Black Tea", "content": 10, "isCommonAllergen": False},
]
coffee_ingredients = [
    {"name": "Water", "content": 70, "isCommonAllergen": False},
    {"name": "Milk", "content": 20, "isCommonAllergen": True},
    {"name": "Ground Java coffee beans", "content": 10, "isCommonAllergen": False},
]
beer_ingredients = [
    {"name": "Water", "content": 60, "isCommonAllergen": False},
    {"name": "Malt", "content": 30, "isCommonAllergen": True},
    {"name": "Ethanol", "content": 8, "isCommonAllergen": True},
    {"name": "Hops", "content": 2, "isCommonAllergen": True},
]
wine_ingredients = [
    {"name": "Grapes", "content": 85, "isCommonAllergen": False},
    {"name": "Ethanol", "content": 15, "isCommonAllergen": True},
]
products_ingredients_by_id = {
    1: tea_ingredients,
    2: coffee_ingredients,
    3: beer_ingredients,
    4: wine_ingredients,
}


@app.route("/product/<product_id>/ingredients")
def get_product_ingredients(product_id):
    print("product_id:", product_id)
    return json.dumps(products_ingredients_by_id[int(product_id)])


@app.route("/order", methods=["POST"])
def post_order():
    json_order_data = request.data
    print("Got data:", json_order_data)
    decoded_json_order_data = json.loads(json_order_data)
    total_price = calculate_total_price(decoded_json_order_data)
    response = {"orderId": 123, "totalPrice": total_price}
    return json.dumps(response)


def calculate_total_price(order_data):
    total = 0
    for order in order_data:
        product = get_product_by_product_id(order["productId"])
        total += product["price"] * order["quantity"]
    return total


def get_product_by_product_id(product_id):
    for p in products:
        if int(product_id) == p["id"]:
            return p
    raise Exception(f"Could not find product for productId:{product_id}")


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response