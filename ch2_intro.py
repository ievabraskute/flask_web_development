from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'''<h1>Hello World!</h1>
              <p>Your browser is {user_agent}</p>'''


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/404')
def not_found():
    return '<h1>Bad Request</h1>', 400


@app.route('/get_response')
def get_response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/redirect')
def my_redirect():
    return redirect('http://www.15min.lt')


@app.route('/userid/<int:id>')
def get_user(id):
    if id > 200:
        abort(404)
    return f'<h1>Hello, {id}</h1>'
