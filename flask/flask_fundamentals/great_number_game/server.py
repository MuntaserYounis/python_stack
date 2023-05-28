from flask import Flask, session, request, render_template,redirect
import random

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
        if 'random' not in session:
            session['random'] = random.randint(1,100)
        if 'myguess' not in session:
            session['myguess'] = 0
        print(session['random'])
        return render_template('index.html', random = session['random'], guess = session['myguess'])
        

@app.route('/process', methods = ['POST'])
def process():
    session['myguess'] = int(request.form['myguess'])
    return redirect('/')

@app.route('/clr', methods = ['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
