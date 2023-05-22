from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return f'hello {name}!'

@app.route('/repeat/<number>/<name>')
def repeat(number,name):
    return f'{name} '* int(number)

@app.errorhandler(404)
def page_not_found(abcd):
    return 'Sorry! No Response. Try again.'

if __name__ == "__main__" :
    app.run(debug=True)