# Python Flows and Loops – Coding Questions

# 1. Write a Python program using an if statement to
# check whether a number is positive.
def prog_1(num):
    return num >= 0

# 2. Write a program using if...else to check whether a
# number is positive or negative.
def prog_2(num):
    return "Negative" if num < 0 else "Positive"

# 3. Write a program using if...elif...else to check whether
# a number is odd or even.
def prog_3(num):
    if num % 2:
        return "odd"
    else:
        return "even"

# 4. Create a program using a for loop to calculate the
# sum of all numbers in the list [1,2,4,5,6].
def prog_4(n):
    sum = 0
    for i in n:
        sum += i
    return sum

# 5. Write a program to iterate the list ['Master','Bridge','
# Python'] using range() and len().
def prog_5(lt):
    for x in range(0,len(lt)):
        print(lt[x])
        
# 6. Write a program using range() to print all numbers
# from 0 to 9.
def prog_6():
    for x in range(0, 10):
        print(x)

# 7. Write a program using for...else to print elements of
# list [0,1,5] and display 'No items left.' at the end.
def prog_7(ls):
    for item in ls:
        print(item)
    print("No items left")

# 8. Write a program using a while loop to add the first N
# natural numbers.
def prog_8(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    print(sum)
    
# 9. Write a program using a break statement to stop the
# loop when value 4 appears in the list [1,2,3,4,5].
def prog_9(ls):
    for item in ls:
        if item == 4:
            break

# 10. Write a program using a continue statement to skip
# value 4 in the list [1,2,3,4,5].
def prog_9(ls):
    for item in ls:
        if item == 4:
            continue
        
# Scenario-Based Questions

# 11. Scenario: User enters a number N. Write code to
# print squares of all non‐negative integers less than N
# using a for loop.
def code_11(n):
    for x in range(n, 0, -1):
        print(x**2)

# 12. Scenario: Create a program to print the
# multiplication table of 7 using a for loop.
def prog_12():
    for i in range(1,11):
        print(i*7)
        
# 13. Scenario: Write a program to generate the Fibonacci
# series using a while loop until 10 terms.
def prog_13():
    n1, n2 = 0, 1
    for i in range(0,10):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
# 14. Scenario: Given list [1,0,1,0,1,1,0,2,3,0,1,0,2],
# remove all elements greater than 1 using a loop.
def loop(ls):
    for item in ls:
        if item > 1:
            ls.remove(item)
            
# 15. Scenario: Write a program to divide two numbers
# without using the '/' operator using repeated
# subtraction.
def div(num, div):
    ct = 0
    while num >= div:
        ct += 1
        num -= div
    return ct