#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    straw = request.form['strawberry']
    raspberry=request.form['raspberry']
    apple = request.form['apple']
    fname=request.form['first_name']
    lname=request.form['last_name']
    count = int(straw)+ int(raspberry)+int(apple)
    print(f'Charging {fname} {lname} for {count} fruits')
    return render_template("checkout.html",straw = straw,apple = apple,raspberry=raspberry,fname=fname,lname=lname,id=request.form['student_id'],count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    