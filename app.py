from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

products = [
    {"id":1,"name":"Headphones","price":49.99,"image":"https://cdn-icons-png.flaticon.com/512/869/869869.png"},
    {"id":2,"name":"Keyboard","price":89.99,"image":"https://cdn-icons-png.flaticon.com/512/2874/2874636.png"},
    {"id":3,"name":"Mouse","price":29.99,"image":"https://cdn-icons-png.flaticon.com/512/2889/2889676.png"},
    {"id":4,"name":"Monitor","price":199.99,"image":"https://cdn-icons-png.flaticon.com/512/1792/1792511.png"}
]

@app.route('/')
def home():
    return render_template("index.html", products=products)

@app.route('/product/<int:id>')
def product(id):

    for p in products:
        if p["id"] == id:
            return render_template("product.html", product=p)

@app.route('/add-to-cart/<int:id>')
def add_to_cart(id):

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect(url_for('product', id=id, added="true"))

@app.route('/remove-from-cart/<int:id>')
def remove_from_cart(id):

    if "cart" in session:
        if id in session["cart"]:
            session["cart"].remove(id)
            session.modified = True

    return redirect(url_for('cart'))

@app.route('/cart')
def cart():

    cart_items = []

    if "cart" in session:
        for id in session["cart"]:
            for p in products:
                if p["id"] == id:
                    cart_items.append(p)

    return render_template("cart.html", cart=cart_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)