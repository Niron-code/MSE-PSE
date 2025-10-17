from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, Flask!</h1>'

@app.route('/bye')
def bye():
    return '<h1>Bye, Flask!</h1>'

@app.route('/username/<name>')
def learn(name):
    return f'<h1>{name} is learning Flask!</h1>'

@app.route('/square/<int:number>')
def calculate_square(number):
    return f'<h1>The square of {number} is {number**2}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)