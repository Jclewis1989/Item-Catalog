from flask import Blueprint, session, jsonify
from item_catalog.models import Item, ItemCategory

json = Blueprint('json', __name__)

# Entire catalog item and details in JSON
@json.route('/items/<int:item_id>/category/JSON')
def itemJSON(item_id):
    items = session.query(Item).filter_by(id=item_id).one()
    itemCategories = session.query(ItemCategory).filter_by(
        item_id=item_id).all()
    return jsonify(itemCategories=[i.serialize for i in itemCategories])

# Every detail of an item category in JSON
@json.route('/items/<int:item_id>/details/<int:details_id>/JSON')
def itemDetailsJSON(item_id, details_id):
    itemDetails = session.query(ItemCategory).filter_by(id=details_id).one()
    return jsonify(itemDetails=itemDetails.serialize)

# Every item category in JSON
@json.route('/items/JSON')
def itemOnlyJSON():
    items = session.query(Item).all()
    return jsonify(items=[i.serialize for i in items])