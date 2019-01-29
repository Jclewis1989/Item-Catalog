from flask import Flask, render_template, url_for, redirect, request, Blueprint, session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from item_catalog.models import Base, User, Item, ItemCategory

posts = Blueprint('posts', __name__)

# Create database connection
engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Items route to show all items
@posts.route('/items/')
def showAll():
    result = engine.execute("SELECT * FROM item")
    #items = session.query(Item).all()
    # Returning every item in the catalog to perform crud operations on
    return render_template('items.html', items = result)

# Create route to create new items in the catalog
@posts.route('/items/new/', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = Item(name=request.form['name'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('posts.showAll'))
    else:
        return render_template('new.html')

# Edit route to edit item names
@posts.route('/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id):
    #editItem = session.query(Item).filter_by(id=item_id).one()
    editedItem = engine.execute("SELECT item.name FROM item WHERE item.id = ?", item_id)
    if request.method == 'POST':
        if request.form['name']:
            editItem.name = request.form['name']
            return redirect(url_for('posts.showAll'))
    else:
        for i in editedItem:
            return render_template('editItem.html', item = i)

# Delete route to delete item names
@posts.route('/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    itemDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemDelete)
        session.commit()
        return redirect(url_for('posts.showAll', item_id = item_id))
    else:
        return render_template('editItem.html', itemDelete = itemDelete)

# Show an Item Details
@posts.route('/items/<int:item_id>/')
@posts.route('/items/<int:item_id>/details/')
def showItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    itemDetails = session.query(ItemCategory).filter_by(item_id = item_id).all()
    return render_template('details.html', itemDetails=itemDetails, item=item)

# Create new details for an item
@posts.route('/items/<int:item_id>/details/new/', methods=['GET', 'POST'])
def newCategory(item_id):
    itemName = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':
        newItem = ItemCategory(description=request.form['description'], category=request.form['category'], name=request.form['name'], price=request.form['price'], stock=request.form['stock'], item_id=item_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('posts.showItem', item_id=item_id))
    else:
        return render_template('newDetails.html', items = itemName, item_id = item_id)

    return render_template('newDetails.html', items = itemName)

# Edit details for a catalog item
@posts.route('/items/<int:item_id>/details/<int:itemDetails_id>/edit', methods=['GET', 'POST'])
def editDetails(item_id, itemDetails_id):
    itemName = session.query(Item).filter_by(id=item_id).one()
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
        return redirect(url_for('posts.showItem', item_id=item_id))
    else:
        return render_template(
            'newDetails.html', item_id=item_id, itemDetails_id=itemDetails_id, item=editedItem, items=itemName)

# Delete details for a catalog item
@posts.route('/items/<int:item_id>/details/<int:itemDetails_id>/delete', methods=['GET', 'POST'])
def deleteDetails(item_id, itemDetails_id):
    itemToDelete = session.query(ItemCategory).filter_by(id=item_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('posts.showItem', item_id=item_id))
    else:
        return render_template('details.html', item=item)