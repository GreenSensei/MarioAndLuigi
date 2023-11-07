from flask import Flask, render_template, request, jsonify, Markup

app = Flask(__name__)

# Sample data for kitchen orders (product quantities and order types)
product_quantities = [
    (1, 0, 0, 3, 2, 0),
    (1, 2, 0, 0, 1, 3),
    (0, 0, 2, 1, 0, 3),
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

# Define order types (0 for "Eat In" and 1 for "Take Out")
order_types = [0, 1, 0]  # Set the order types to "Eat In" by default

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

@app.route('/')
def index():
    orders = generate_orders(product_quantities, product_prices, order_types)

    for order in orders:
        order['product_name'] = Markup(order['product_name'])  # Use Markup to render HTML safely

    return render_template('index.html', orders=orders, order_types=order_types)

@app.route('/mark_order_ready', methods=['POST'])
def mark_order_ready():
    order_id = int(request.form.get('order_id'))
    # Here, you can add your logic to mark the order as "Ready" (e.g., update a database)
    # For demonstration purposes, we'll just return a JSON response
    return jsonify({'message': f'Order #{order_id} marked as ready'})

if __name__ == '__main__':
    app.run(debug=True)
