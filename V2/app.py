from flask import Flask, render_template

app = Flask(__name__)

# Sample data for menu items (you can replace this with your own data)
menu_items = [
    {"name": "Margherita Pizza", "price": 10},
    {"name": "Salami Pizza", "price": 11},
    {"name": "Hawaii Pizza", "price": 12},
    {"name": "Meatlovers Pizza", "price": 13},
    {"name": "Pepperoni Pizza", "price": 11},
    {"name": "Veggie Pizza", "price": 13},
]

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
