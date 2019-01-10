from flask import Flask, render_template, url_for, request, redirect, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item, ItemCategory

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Serialize JSON
@app.route('/items/<int:item_id>/category/JSON')
def itemCategoryJSON(item_id):
    items = session.query(Item).filter_by(id=item_id).one()
    itemCategories = session.query(ItemCategory).filter_by(
        item_id=item_id).all()
    return jsonify(itemCategories=[i.serialize for i in items])

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
        session.commit()
        session.rollback() #Running into errors if this code is not present
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
    itemDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemDelete)
        session.commit()
        return redirect(url_for('showAll', item_id = item_id))
    else:
        return render_template('editItem.html', itemDelete = itemDelete)

# Show an Item Details
@app.route('/items/<int:item_id>/')
@app.route('/items/<int:item_id>/details/')
def showItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    itemDetails = session.query(ItemCategory).filter_by(item_id = item_id).all()
    return render_template('details.html', itemDetails=itemDetails, item=item)

# Create new details for an item
@app.route('/items/<int:item_id>/details/new/', methods=['GET', 'POST'])
def newCategory(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        newItem = ItemCategory(description=request.form['description'], category=request.form['category'], name=request.form['name'], price=request.form['price'], stock=request.form['stock'], item_id=item_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showItem', item_id=item_id))
    else:
        return render_template('newDetails.html', item=item, item_id = item_id)

    return render_template('newDetails.html', item=item)

# Edit details for a catalog item
@app.route('/items/<int:item_id>/details/<int:itemDetails_id>/edit', methods=['GET', 'POST'])
def editDetails(item_id, itemDetails_id):
    editedItem = session.query(ItemCategory).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['category']:
            editedItem.category = request.form['category']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['stock']:
            editedItem.stock = request.form['stock']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showItem', item_id=item_id))
    else:

        return render_template(
            'newDetails.html', item_id=item_id, itemDetails_id=itemDetails_id, item=editedItem)

# Delete details for a catalog item
@app.route('/items/<int:item_id>/details/<int:itemDetails_id>/delete', methods=['GET', 'POST'])
def deleteDetails(item_id, itemDetails_id):
    itemToDelete = session.query(ItemCategory).filter_by(id=item_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST': # Post must come from a form, not href! Fix later today
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItem', item_id=item_id))
    else:
        return render_template('details.html', item=item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)