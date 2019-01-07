from flask import Flask, render_template, url_for, request, redirect, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item, ItemCategory

app = Flask(__name__)

engine = create_engine('sqlite:///itemCatalog.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Index route to home page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# Items route to show all items
@app.route('/items/')
def showAll():
    items = session.query(Item).all()
    # Returning every item in the catalog to perform crud operations on
    return render_template('items.html', items = items)

# Create route to create new items in the catalog
@app.route('/items/new/', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = Item(name=request.form['name'])
        session.add(newItem)
        session.flush()
        session.commit()
        return redirect(url_for('showAll'))
    else:
        return render_template('new.html')

# Edit route to edit item names
@app.route('/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id):
    editItem = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
            return redirect(url_for('showAll'))
    else:
        return render_template('editItem.html', item = editItem)

# Delete route to delete item names
@app.route('/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    itemDelete = session.query(
        Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemDelete)
        session.commit()
        return redirect(
            url_for('showAll', item_id = item_id))
    else:
        return render_template(
            'editItem.html', itemDelete = itemDelete)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)