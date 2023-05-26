from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'secret_key'
@app.route('/')
def index():
    
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html',visit_count = session['counter'])

@app.route('/destroy_session', methods = ['POST']   )
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
