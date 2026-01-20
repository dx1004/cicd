# Namespace and Variables - Coding Questions

# 1. Write a Python program to assign a = 2 and print its memory address using id().
def p1():
    a = 2
    print(id(a))
    
# 2. Create two variables a = 5 and b = a. Print id(a) and id(b) and show they refer to same object.
def p2():
    a, b = 5, a
    
# 3. Write code to demonstrate dynamic binding by assigning integer, string and list to same variable one after another and print its type each time.
def p3():
    def ppt(val):
        print(f'The type of {val} is {type(val)}')
    a = 1
    ppt(a)
    a = "string"
    ppt(a)
    a = [1,2,3,4]
    ppt(a)
    
# 4. Write a program that defines a global variable x = 10 and prints it inside a function without using the global keyword.
def p4():
    global x
    x = 10
    def afunction():
        print(x)
    afunction()
    
# 5. Create a function with a local variable y = 20 and print y inside the function. Try printing y outside and show the error in the comment.
def p5():
    def func():
        y = 20
        print(y)
    func()
#    print(y) #NameError: name 'y' is not defined
    
# 6. Write a nested function where the inner function has variable a = 30 and the outer has a = 20. Print both values, similar to a logic question in a PowerPoint presentation.
def p6():
    def outer():
        a = 20
        def inner():
            a = 30
            print(a)
        inner()
        print(a)
    outer()
    
# 7. Write code using the global keyword inside a function to modify global variable a from 10 to 20 and print before and after.
def p7():
    a = 20
    def func():
        global a
        a = 10
    print(a)
    func()
    print(a)

# 8. Demonstrate UnboundLocalError by trying to modify a global variable inside a function without using the global keyword (write expected error as a comment).
def p8():
    a = 10
    def func():
        a += 5
    func() #UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    
# 9. Create a file config.py style example in a single script using variables a=10, b=15 and access them using a simulated module object (use a class to mimic).
def p9():
    class Config:
        a, b = 10, 15
    config = Config
    print(f'Accessing config.a: {config.a}')
    print(f'Accessing config.b: {config.b}')
    
# 10. Write an example using the import style concept: create two functions, add() and sub(), in the same file and call them using the alias name m.
def p10():
    class m:
        @staticmethod
        def add():
            return "add"
        @staticmethod
        def sub():
            return "sub"
    print(m.add())
    print(m.sub())

# Part B Scenario Based Qusetions

# 11. Scenario: A company program has a global tax rate of 5. Create a function calculate() that changes tax_rate to 10 using the global keyword and compute price*tax_rate.
def p11():
    trate = 5
    def calculate(price):
        global trate
        trate = 10
        return trate * price
        
# 12. Scenario: In the school system outer function has school='ABC' and the inner function wants to modify it to 'XYZ' using nonlocal. Write code.
def p12():
    def outer():
        school = 'ABC'
        def inner():
            global school
            school = 'XYZ'

# 13. Scenario: Developer created counter=0 globally. Write a function increment() that increases the counter by 1 each call using a global.
def p13():
    counter = 0
    def increment():
        global counter
        counter += 1

# 14. Scenario: Module config has a=100. Another module modifies changes a to 200 and main prints it. Write combined code in a single file representation.
def p14():
    class ModuleConfig:
        a = 100
    config = ModuleConfig
    
    def another():
        config.a = 200
        
    def main():
        print(f"Main Start: config.a is {config.a}")
    
        # Trigger the change from the other 'module'
        another()
    
        # Check if the change is reflected here
        print(f"Main End: config.a is now {config.a}")
    
    if __name__ == "__main__":
        main()
        

# 15. Scenario: Create nested functions representing company->department->team, where team changes department name using nonlocal and print all values.
def p15():
    def company():
        company_name = "Company Name"
        
        def department():
            department_name = "Dname"
            
            def team():
                nonlocal department_name
                department_name = "New name"
                print(f"Team Level: Updated department to '{department_name}'")
        
            print(f"Dept Level (Before): {department_name}")
            team()
            print(f"Dept Level (After): {department_name}")
        
        print(f"Company Level: {company_name}")
        department()

    company()