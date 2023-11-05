from flask import Flask, render_template, request, jsonify, Markup

app = Flask(__name__)

# Sample data for kitchen orders (product IDs and quantities)
product_quantities = [0, 0, 0, 2, 2, 0]

# Define the prices for each product
product_prices = {
    'Margherita Pizza': 9.99,
    'Salami Pizza': 10.99,
    'Hawaii Pizza': 11.99,
    'Meatlovers Pizza': 12.99,
    'Pepperoni Pizza': 10.99,
    'Veggie Pizza': 12.99,
}

# Function to generate a single order with consolidated quantities
def generate_orders(product_quantities, product_prices):
    order = {
        'id': 1,  # You can set a unique order ID here
        'product_name': '<br>',
        'total_price': 0,
    }

    products = list(product_prices.keys())

    for product_quantity in zip(products, product_quantities):
        product_name, quantity = product_quantity
        if quantity > 0:
            price = product_prices.get(product_name, 0.0)  # Retrieve the price from the dictionary

            formatted_product = f"{quantity}x {product_name}<br>"
            order['product_name'] += formatted_product
            order['total_price'] += price * quantity

    return [order]

@app.route('/')
def index():
    orders = generate_orders(product_quantities, product_prices)
    # Use Markup to render HTML safely
    for order in orders:
        order['product_name'] = Markup(order['product_name'])
    return render_template('index.html', orders=orders)

@app.route('/mark_ready/<int:order_id>', methods=['POST'])
def mark_order_ready(order_id):
    # Here, you can add your logic to mark the order as "Ready" (e.g., update a database)
    # For demonstration purposes, we'll just return a JSON response
    return jsonify({'message': f'Order #{order_id} marked as ready'})

if __name__ == '__main__':
    app.run(debug=True)
