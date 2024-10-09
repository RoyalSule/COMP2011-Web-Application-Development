from flask import render_template
from app import app

@app.route('/fruit.html')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit.html", fruits=fruits)

@app.route('/')
def index():
    user = {'name': 'Homer Simspon'}
    return render_template('index.html', user=user)
