from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

# 🛒 cart (dictionary for quantity)
cart = {}

# 🥦 products with price
products = {
    "Tomato": 20,
    "Potato": 30,
    "Onion": 25
}

# 🔐 LOGIN PAGE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/home')
    return render_template('login.html')


# 🏠 HOME PAGE
@app.route('/home')
def home():
    return render_template('index.html')


# ➕ ADD TO CART
@app.route('/add_to_cart/<item>')
def add_to_cart(item):
    if item in products:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    return redirect('/cart')


# ➖ REMOVE ITEM
@app.route('/remove/<item>')
def remove(item):
    if item in cart:
        cart[item] -= 1
        if cart[item] <= 0:
            del cart[item]
    return redirect('/cart')


# 🛒 CART PAGE
@app.route('/cart')
def show_cart():
    total = 0
    for item, qty in cart.items():
        total += products[item] * qty
    return render_template('cart.html', cart=cart, products=products, total=total)


# 🚀 RUN FOR RENDER (IMPORTANT)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
