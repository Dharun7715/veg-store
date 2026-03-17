from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

cart = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/add_to_cart/<item>")
def add_to_cart(item):
    cart.append(item)
    return redirect(url_for("cart_page"))

@app.route("/cart")
def cart_page():
    return render_template("cart.html", cart=cart)

@app.route("/remove/<item>")
def remove(item):
    if item in cart:
        cart.remove(item)
    return redirect(url_for("cart_page"))

# 🔥 VERY IMPORTANT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
