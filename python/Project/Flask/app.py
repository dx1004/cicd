from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

'''
Flask – Problem Statement 1 
Student Feedback CollecƟon System 
Problem DescripƟon: 
Create a Flask web applicaƟon that allows students to submit feedback for a course. 
FuncƟonal Requirements: 
1.  Display a web form with the following fields: 
o  Student Name 
o  Email ID 
o  Course Name (dropdown) 
o  Feedback (textarea) 
2.  On clicking Submit: 
o  The data should be sent to the Flask backend using POST 
o  The submiƩed data should be displayed on a new page 
3.  Add a Reset buƩon to clear the form.
'''

@app.route('/')
def index():
    base_url = request.url_root.rstrip('/')
    routes = []
    routes.append('├─ <a href="/feedback">Student Feedback Collection System</a>')
    routes.append('├─ <a href="/feedback_mod">Modified Student Feedback Collection System</a>')
    routes.append('├─ <a href="/checker">Temperature Status Checker Application</a>')
    
    return f'''
    <pre style="font-family: monospace; font-size: 18px; line-height: 1.6;">
    
Flask App Routes
{chr(10).join(routes)}
    </pre>
    '''
    return tree

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Get form data
        feedback ={
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "course" : request.form.get('course'),
            "feedback" : request.form.get('feedback')
        }
        return render_template("display.html", feedback = feedback)
    
    return render_template("feedback.html")
        
@app.route('/feedback_mod', methods=['GET', 'POST'])
def feedback_mod():
    if request.method == 'POST':
        # Get form data
        feedback ={
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "course" : request.form.get('course'),
            "feedback" : request.form.get('feedback')
        }
        return render_template("display.html", feedback = feedback)
    
    return render_template("feedback.html", mod = True)


'''
Flask - Problem Statement 2 
Temperature Status Checker ApplicaƟon 
Problem DescripƟon: 
Develop a Flask applicaƟon that accepts temperature input from the user and displays the 
environmental status. 
FuncƟonal Requirements: 
1.  Create a form to input: 
o  Temperature value (in °C) 
2.  AŌer submission: 
o  Display: 
  “Cold” if temperature < 20 
  “Normal” if temperature between 20-30 
  “Hot” if temperature > 30 
3.  Display the result on the same page. 
'''
@app.route('/checker', methods=['GET', 'POST'])
def checker():
    eva = None
    if request.method == 'POST':
        temp = int(request.form.get("temp"))
        if temp < 20:
            eva = "Cold 🥶"
        elif temp > 30:
            eva = "Hot 🥵"
        else: eva = "Normal 😌"
    return render_template("checker.html", result = eva)

if __name__ == '__main__':
    app.run(debug=True)
