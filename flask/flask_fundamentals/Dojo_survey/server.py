from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def process():
    
    return render_template('output.html',name = request.form['name'],loc = request.form['location'],fav = request.form['language'],comment = request.form['comment'])
if __name__ == '__main__':
    app.run(debug=True)