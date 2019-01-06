from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)