from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

cart = []

# 🔐 LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/home")
    return render_template("login.html")

# 🏠 HOME PAGE
@app.route("/home")
def home():
    return render_template("index.html")

# 🛒 ADD TO CART
@app.route("/add_to_cart/<item>")
def add_to_cart(item):
    cart.append(item)
    return redirect("/cart")

# 🧾 CART PAGE
@app.route("/cart")
def cart_page():
    return render_template("cart.html", cart=cart)

# ❌ REMOVE ITEM
@app.route("/remove/<item>")
def remove(item):
    if item in cart:
        cart.remove(item)
    return redirect("/cart")

# 🚀 RENDER DEPLOY FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
