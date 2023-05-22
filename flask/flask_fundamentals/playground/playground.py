from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/') #the '/' after play (question)
def index():
    return render_template('index.html')

@app.route('/play/<x>')
def display(x):
    return render_template('play.html',repeats = int(x))

@app.route('/play/<x>/<color>')
def display_color(x,color):
    return render_template('play.html',repeats = int(x),my_color = color)
if __name__ == '__main__':
    app.run(debug =True) #still shwoing errors
    
