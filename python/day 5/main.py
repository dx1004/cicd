'''1. Write a Python function named hello(name)
that prints a greeting message using the name
parameter.'''
def hello(name):
    print("You have been greeted,",name)

'''2. Write a function new_line() that prints an empty
line and demonstrate calling it between two print
statements.'''
def new_line():
    print()
    
'''3. Write a function sum(a, b) that returns the sum
of two numbers and print the result.'''
def sum(a,b):
    return(a+b)

'''4. Write a program to demonstrate the scope of
variables using a local variable x inside a function
and a global x outside.'''
def demo(x=5):
    print(x)

'''5. Write a function to find the maximum of three
numbers.'''
def max(a,b,c):
    return max(a,b,c)

'''6. Write a Python function to check whether a
number is in a given range.'''
def inRange(a):
    return(a>0 & a<20)

'''7. Write a function using default arguments to
add two numbers, where the second argument
has a default value of 10.'''
def add_num(a, b=10):
    return a+b

'''8. Write a function using arbitrary arguments
(*names) to print a greeting for multiple names.'''
def greet(*names):
    for name in names:
        print("Hello,",name)
     
'''9. Write a recursive function to calculate the
factorial of a number.'''   
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

'''10. Write a lambda function to find the cube of a
number and call it.'''
cube = lambda x: x ** 3
print(cube(4))

'''1. A program has a function defined but never
called. Explain what will happen according to the
flow of execution.'''
# python interpreter reads and exec the def statement, creates a function object
# the body is not exec, no result will output from the function

'''2. A developer used a return statement without
an expression in a function. What value will be
returned?'''
# returns None

'''3. You created a variable inside a function and
tried to access it outside. Explain the result
based on the scope.'''
# you can not access it outside, local scope variable can only be accessed locally

'''4. A function is called with fewer arguments than
defined. Explain using the fixed and default
argument concept.'''
# function will give error if fewer arguments than
# defined. however if default argument exisit, function can run

'''5. A team wants to reuse the same logic multiple
times. Which concept from the slides should they
use and why?'''
# warp the code in a function

'''6. A function receives a list and modifies it. Will
the original list change? Explain using pass by
reference concept.'''
# yes, the global variable is been modified

'''7. A programmer created an alias for a function
name. How does aliasing help, according to the
slides?'''
# helps the programmer easier to read it

'''8. You need to double all elements of a list. Which
concept map() or filter() is suitable and why?'''
# map() executes a specified function for each item in an iterable

'''9. A requirement is to get only even numbers
from the list. Which function should be used
based on the slides?'''
# filters()

'''10. A function is defined inside another function.
What is this called, and what advantage does it
give?'''
# nested function, information hiding, code organization
