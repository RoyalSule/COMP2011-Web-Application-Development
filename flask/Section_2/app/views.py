from flask import render_templatec
from app import app

@app.route('/')
def index():
    user = {'name': 'Homer Simspon'}
    return render_template('index.html', title='Simple template example', user=user)