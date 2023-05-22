from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkboard(columns=8,rows = 8):
    return render_template('index.html',columns=columns,rows=rows)

@app.route('/<x>/')
def checkboard_columns(x=8,rows = 8):
    return render_template('index.html',columns=int(x),rows=rows)
@app.route('/<x>/<y>')
def checkboard_rows(y,x=8):
    return render_template('index.html',columns=int(x),rows = int(y))


if __name__ == '__main__':
    app.run(debug=True)

