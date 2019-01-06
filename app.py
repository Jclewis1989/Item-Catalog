from flask import Flask, render_template, url_for, request, redirect, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item, ItemCategory

app = Flask(__name__)

engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/items')
def showAll():
    items = session.query(Item).all()
    # Returning every item in the catalog to perform crud operations on
    return render_template('items.html')

@app.route('/items/new/', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = Item(name=request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('items'))
    else:
        # Create a new item
        return render_template('new.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)