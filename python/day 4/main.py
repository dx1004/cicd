import math

def q1(a,b,c):
    '''1. Arithmetic Mastery: Given three sides of a triangle, a,
    b, and c, write a Python script to calculate the semi-
    perimeter $s$ and then the area of the triangle using
    the provided formula: area = sqrt{s(s-a)(s-b)(s-c)}.'''
    s = a+b+c
    area = math.sqrt(s(s-a)(s-b)(s-c))
    
def q2():
    # 2. Floor Division: What is the output of the expression 9
    # // 2 in Python? Explain what the // operator does?.
    print(9//2) # // rounds off the decimal
    
def q3():
    # 3. String Concatenation: If a = "Hello" and b = "World",
    # what will print(a + b) display? Explain the role
    a = "Hello"; b = "World"
    print(a+b) # this will print HelloWorld, + will concat the string
    

'''4. Logical Operations: If x = True and y = False, what are
the results of the following expressions?
    o x and y -> False
    o x or y -> True
    o not x -> False '''
    
def q5():
    # 5. Membership Testing: Using Python membership
    # operators, write an expression to check if the value 5
    # exists in a sequence named x.
    x = [1,2,43,5,6]
    print(5 in x) # this will print is 5 is in x
    
def q6():
    # 6. Formatted String Literals: Create a script that assigns
    # "Python" to a variable named subject and uses an f-
    # string to print: "We are learning Python."
    subject = "Python"
    print(f"We are learning {subject}")
    
# 7. Modulo and Exponentiation: Calculate the output for
# the following operations: 
#   o 10 % 3 -> 1
#   o 10 ** 3 -> 1000

# 8. The eval() Function: Why is using eval(input())
# considered a "security hole" according to the slides?
# Provide an example of a dangerous command a user
# could enter.

# Using eval(input()) is considered a security hole because 
# it allows for arbitrary code execution

def q9():
    # 9. Old Style Formatting: Given x = 3.75, write a print
    # statement using the % interpolation operator to
    # display the value as: "You have $3.75 in your pocket".
    print("You have $%f in your pocket" %(3.75))
    
# 10. Identity vs. Equality: Explain the purpose of the
# is operator and how it differs from == based on the
# identity operator definitions.

# is operator checks memory address, == checks data

# Problem 1: Monthly Expense Splitter
# Scenario:
# A group of friends share a monthly apartment expense. 
# The total expensemust be divided equally.
# 
# Input
# Enter total expense: 2350
# Enter number of friends: 6
# 
# Task
# Print:
# The amount each friend should pay
# Remaining amount (if any)
# Expected Output
# 391
# 4
def p1():
    total = 2350
    nf = 6
    print(total/nf,total%nf,sep="\n")

# Problem 2: Exam Pass Evaluation
# Scenario:
# A student must score 50 or more to pass anexam.
# 
# Input
# Enter marks: 49.5
# 
# Task
# Print:
# Whether the student passed
# The data type of the marks entered
# 
# Expected Output
# False
# float
def p2():
    mk = 49.5
    print(mk>=50,type(mk),sep="\n")
    
# Problem 3: Online Shopping Final Bill
# Scenario:
# An online store gives a discount and then
# adds tax.
# 
# Input
# Enter price: 1500
# Enter discount percentage: 10
# Enter tax percentage: 5
# 
# Task
# Calculate and print the final bill amount.
# 
# Expected Output
# 1417.5
def p3():
    price = 1500
    dsct = 10
    tax = 5
    print(price*(1-dsct/100)*(1+tax/100))
    
# Problem 4: Smart Water Tank Monitor
# Scenario:
# A water tank has a fixed capacity. Sensors
# report the current water level.
# 
# Input
# Enter tank capacity: 1000
# Enter current water level: 1000
# 
# Task
# Print:
# Remaining capacity
# Whether the tank is full
# 
# Expected Output
# 0
# True
def p4():
    print(1000-1000,1000==1000,sep="\n")
    
# Problem 5: Mobile Data Overuse Checker
# Scenario:
# A telecom provider charges extra if data
# usage exceeds the daily limit.
# 
# Input
# Enter daily limit (GB): 1.5
# Enter used data (GB): 2.2
# 
# Task
# Print:
# Extra data used
# Whether extra charges apply
# 
# Expected Output
# 0.7
# True
def p5():
    print(round((2.2-1.5),1),1.5<=2.2,sep="\n")
    
