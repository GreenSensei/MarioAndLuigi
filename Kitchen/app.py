from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

# Initialize product_quantities as an empty list
product_quantities = [
    (1, 0, 0, 3, 2, 0),
    (1, 2, 0, 0, 1, 3),
    (1, 0, 0, 0, 0, 1),
]

# Define the prices for each product
product_prices = {
    'Margherita Pizza': 9.99,
    'Salami Pizza': 10.99,
    'Hawaii Pizza': 11.99,
    'Meatlovers Pizza': 12.99,
    'Pepperoni Pizza': 10.99,
    'Veggie Pizza': 12.99,
}

menu_items = [
    {"name": "Margherita Pizza", "price": 9.99},
    {"name": "Salami Pizza", "price": 10.99},
    {"name": "Hawaii Pizza", "price": 11.99},
    {"name": "Meatlovers Pizza", "price": 12.99},
    {"name": "Pepperoni Pizza", "price": 10.99},
    {"name": "Veggie Pizza", "price": 12.99},
]

# Define order types (0 for "Eat In" and 1 for "Take Out")
order_types = [0, 1, 0]  # Set the order types to "Eat In" by default
order_id_counter = 1

# Function to generate orders based on product quantities and prices
def generate_orders(product_quantities, product_prices, order_types):
    orders = []

    for order_id, (product_quantity, order_type) in enumerate(zip(product_quantities, order_types), start=1):
        if order_type == 1:
            order_type_text = 'Take Out'
        else:
            order_type_text = 'Eat In'

        order = {
            'id': order_id,
            'product_name': '',
            'total_price': 0,
            'order_type': order_type_text,
        }

        for product_index, quantity in enumerate(product_quantity, start=1):
            if quantity > 0:
                product_name = list(product_prices.keys())[product_index - 1]  # Retrieve the product name
                price = product_prices.get(product_name, 0.0)  # Retrieve the price from the dictionary

                formatted_product = f"{quantity}x {product_name}"
                if order['product_name']:
                    order['product_name'] += "<br>"  # Add a line break before the next product
                order['product_name'] += formatted_product
                order['total_price'] += price * quantity

        orders.append(order)

    return orders

@app.route('/kitchen.html')
def kitchen():
    orders = generate_orders(product_quantities, product_prices, order_types)

    for order in orders:
        order['product_name']

    return render_template('kitchen.html', orders=orders, order_types=order_types)


@app.route('/complete_order', methods=['POST'])
def complete_order():
    data = request.get_json()
    quantities = data.get('quantities')

    # Generate a new order with an incremented order ID
    global order_id_counter  # Use the global order_id_counter variable
    order = {
        'id': order_id_counter,  # Use the current order ID
        'product_quantities': quantities,
    }

    product_quantities.append(order)
    
    # Increment the order ID counter for the next order
    order_id_counter += 1
    
    # Return a JSON response (for demonstration purposes)
    return jsonify({'message': 'Order marked as complete'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start.html')
def start():
    return render_template('start.html')

@app.route('/menu.html')
def menu():
    return render_template('menu.html')

@app.route('/menutakeout.html')
def menutakeout():
    return render_template('menutakeout.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True)
