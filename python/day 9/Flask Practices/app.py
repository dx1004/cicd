from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Flask PracƟce 1: Route Basics 
# Task: 
# Create a Flask app with 3 routes: 
#   / → displays “Welcome to Flask” 
#   /about → displays your name 
#   /contact → displays your email 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about(): 
    return "Cloud Xu"

@app.route('/contact')
def contact():
    return "cloud.xuan.xu@gmail.com"

# Flask PracƟce 2: Variable in URL 
# Task: 
# Create a route /hello/<name> that displays: 
# Hello, <name>!
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

# Flask PracƟce 3: GET vs POST 
# Task: 
# Create a page with: 
#   A form that takes one number 
#   On submit, display the square of the number
@app.route('/square', methods=['GET', 'POST'])
def square():
    result = None
    
    if request.method == 'POST':
        num = request.form.get('number')
        if num:
            result = int(num) ** 2
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Square Calculator</title>
    </head>
    <body>
        <h1>Square Calculator</h1>
        <form method="POST">
            <input type="number" name="number" placeholder="Enter a number" required>
            <button type="submit">Calculate Square</button>
        </form>
        
        {f'<h2>Result: {result}</h2>' if result is not None else ''}
    </body>
    </html>
    """
    
# Flask Practice 4: Template Rendering 
# Task: 
# Create an HTML template and pass: 
#   Your name 
#   Current year 
# Display them in the template.    
@app.route('/display')
def display():
    return render_template('template.html', name = "Cloud Xu", year = datetime.now().year)

# Flask PracƟce 5: If–Else in Template 
# Task: 
# Pass a temperature value from backend. 
# Display: 
#   “Hot” if > 30 
#   “Normal” otherwise 
@app.route('/temp')
def temp():
    temp = 30
    return "Hot" if temp > 30 else "Normal"

# Flask Practice 6: Loop in Template 
# Task: 
# Pass a list of subjects from Flask. 
# Display them using a loop in HTML. 
@app.route('/loop')
def loop():
    lis = [1,2,3,4,5,6]
    return render_template('loop.html', list=lis)

if __name__ == '__main__':
    app.run(debug=True)