from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# 🛒 cart storage
cart = []

# 🥦 products with price
products = {
    "Tomato": 20,
    "Potato": 30,
    "Onion": 25
}

# 🔐 LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/home')
    return render_template('login.html')


# 🏠 HOME PAGE
@app.route('/home')
def home():
    return render_template('index.html', products=products)


# ➕ ADD TO CART
@app.route('/add_to_cart/<item>')
def add_to_cart(item):
    cart.append(item)
    return redirect('/cart')


# ❌ REMOVE ITEM
@app.route('/remove/<item>')
def remove(item):
    if item in cart:
        cart.remove(item)
    return redirect('/cart')


# 🛒 CART PAGE
@app.route('/cart')
def show_cart():
    total = 0
    for item in cart:
        total += products[item]

    return render_template('cart.html', cart=cart, total=total)


if __name__ == '__main__':
    app.run(debug=True)
