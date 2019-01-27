from flask import Flask, render_template, Blueprint

main = Blueprint('main', __name__)

# Index route to home page
@main.route('/')
@main.route('/home')
def index():
    return render_template('index.html')