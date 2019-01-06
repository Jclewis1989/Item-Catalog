from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/items')
def showAll():
    items = session.query(Item).all()
    # Returning every item in the catalog to perform crud operations on
    return render_template('items.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)