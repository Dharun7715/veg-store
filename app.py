from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cart = []
logged_in = False

products = {
    "Tomato": 20,
    "Potato": 30,
    "Carrot": 40,
    "Apple": 120
}

# Main page (Login + Shop)
@app.route("/", methods=["GET", "POST"])
def main():
    global logged_in

    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == "admin" and pwd == "1234":
            logged_in = True

    total = sum(products[item] for item in cart)
    return render_template("index.html", logged_in=logged_in, cart=cart, total=total)

# Add item → redirect to cart page
@app.route("/add/<item>")
def add(item):
    cart.append(item)
    return redirect("/cart")

# Remove item
@app.route("/remove/<item>")
def remove(item):
    if item in cart:
        cart.remove(item)
    return redirect("/cart")

# Cart page
@app.route("/cart")
def cart_page():
    total = sum(products[item] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

# Logout
@app.route("/logout")
def logout():
    global logged_in
    logged_in = False
    cart.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)