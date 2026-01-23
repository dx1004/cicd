from django.shortcuts import render
from django.http import HttpResponse

# Django PracƟce 1: Project & App Structure 
# Task: 
# Create a Django project and one app. 
# Display: 
# This is my first Django ap
def home(request):
    return HttpResponse("This is my first Django app")

# Django PracƟce 2: Multiple URLs 
# Task: 
# Create three URLs: 
#   / 
#   /about 
#   /services 
# Each should display a different message
def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is the service page")

# Djago PracƟce 3: Template Rendering 
# Task: 
# Create an HTML template and render it from a view. 
def render_temp(request):
    return render(request, '3.html')

# Django Practice 4: Passing Data to Template 
# Task: 
# Pass your name and college name from view to template. 
def name(request):
    content = {
        'name': 'cloud xu',
        'college': 'Cal Poly Pomona'
    }
    return render(request, 'name.html', content)

# Django Practice 5: If–Else in Template 
# Task: 
# Pass a number to the template. 
# Display: 
#   “Even” or “Odd”
def number(request):
    num = 16
    return render(request, "number.html", number = num)

# Django Practice 6: For Loop in Template 
# Task: 
# Pass a list of programming languages and display them. 
def lang(request):
    content = ['python', 'Javascript', 'C', 'Golang', 'Rust', 'C#', 'Java']
    return render(request, "number.html", languages = content)

# Django Practice 7: Form Basics (No DB) 
# Task: 
# Create a form with one input field. 
# On submit, display the entered value on the same page.
def form(request):
    result = None
    if request.method == "POST":
        result = request.POST.get('user_input')
        
    context = {
        'result' : result
    }
    
    return render(request, 'form.html', context)