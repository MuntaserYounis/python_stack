from flask import Flask, redirect, render_template, session,request
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key="Secret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']= 0
        session['list']= []
        session['counter']=0
    gold = session['gold']
    return render_template('index.html',gold = gold , activity_list= session['list'])

@app.route('/clear' , methods= ['POST'])
def clear():
        session.clear()
        return redirect("/")
@app.route('/process', methods = ['POST'])
def process():
    if request.form['building'] =='farm':
        amount = random.randint(10,20)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'earned {amount} golds from farm! {timestamp}'
    elif request.form['building'] =='cave':
        amount = random.randint(5,10)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'earned {amount} golds from Cave! {timestamp}'
    elif request.form['building'] =='house':
        amount = random.randint(2,5)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        text = f'earned {amount} golds from House! {timestamp}'
    elif request.form['building'] =='casino':
        amount = random.randint(-50,50)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p") 
        if amount > 0:
            text = f'earned {amount} golds from Casino!{timestamp}'
        elif amount < 0:
            text = f'lost {amount} golds from Casino!{timestamp}'
        else:
            text = 'You earned nothing'
    session['counter'] +=1
    print(session['counter'])
    session['list'].insert(0,text)
    session['gold'] += amount
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)
