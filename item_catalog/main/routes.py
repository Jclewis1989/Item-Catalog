from flask import Flask, render_template, session, request, Blueprint
from item_catalog.models import Base, Item, ItemCategory

main = Blueprint('main', __name__)

# Index route to home page
@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')