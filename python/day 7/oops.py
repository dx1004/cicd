#OOPS – Coding Questions

# 1. Write a Python class Dog with class variable species and instance variables
# name and age. Create an object and print all attributes.
def p1():
    class Dog:
        species = "animal"
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
    my_dog = Dog("Blacky", 3)
    print("Class variable:")
    print(f"Species: {my_dog.species}")
    print("\nInstance variables:")
    print(f"Name: {my_dog.name}")
    print(f"Age: {my_dog.age}")
    
# 2. Create a class Student with a constructor that initialises name and marks.
# Create an object and display the values.
def p2():
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks
        
        def display(self):
            print(f"Student Name: {self.name}")
            print(f"Marks: {self.marks}")
        
    student1 = Student("Alice Johnson", 85)
    # Display the values
    print("Student Information:")
    student1.display()
    
# 3. Write a program to demonstrate the use of the self parameter inside a class
# method.
''' Refer to p2() '''

# 4. Create a class Animal and inherit it using a Dog class. Call a method from the
# parent class using the child object.
def p4():
    class Animal:
        def __init__(self, name):
            self.name = name
        def display(self):
            print(self.name)
    class Dog(Animal):
        def __init__(self, name, type):
            super().__init__(name)
            self.type = type
    dog1 = Dog("blacky", "unknown")
    dog1.display()
        
# 5. Write a Python program demonstrating single inheritance using two classes.
''' refer to p4() '''

# 6. Write a program to demonstrate method overriding using a parent class and a
# child class.
def p6():
    class parent:
        def __init__(self, name):
            self.name = name
            
        def dipslay(self):
            print(self.name)
            
    class child(parent):
        def __init__(self,name, a1, a2):
            super().__init__(name)
            self.a1 = a1
            self.a2 = a2
        def display(self):
            super().display()
            print(self.a1,self.a2)
            
# 7. Create a class Calculator with a method add() that accepts multiple arguments
# using *args.
def p7():
    class Calculator:
        def add(self, *args):
            """
            Add multiple numbers using *args
            *args allows the method to accept any number of arguments
            """
            return sum(args)

# 8. Write a program to demonstrate operator overloading using the __add__
# method.
def p8():
    class point:
        def __init__(self, x, y):
            self.x = x 
            self.y = y
            
        def __add__(self, other):
            return point(self.x+other.x, self.y+other.y)

# 9. Create a class demonstrating encapsulation using public, protected, and
# private variables.
def p9():
    class demo:
        def __init__(self, a, b, c, d, e):
            self.a = a
            # protected variable
            self._b = b
            self._c = c
            # private variable
            self.__d = d
            self.__e = e

# 10. Write a program using an abstract class with one abstract method and one
# concrete method.
from abc import ABC, abstractmethod
def p10():
    class parent(ABC):
        def __init__(self, name):
            self.name = name
        
        @abstractmethod
        def abs(self):
            pass
        
        # concrete method
        def con(self):
            self.abs()
            
    class child(parent):
        def __init__(self, name):
            super().__init__(name)
            
        def abs(self):
            print(self.name)

# PartB: Scenario-Based Questions

# 11. Scenario: Create a class Vehicle and a child class Car where Car overrides a
# method to display its own behaviour.
def p11():
    class Vehicle:
        def method(self):
            return
        
    class Car(Vehicle):
        def method(self):
            print("this is the overwrite")
            return 1
    
# 12. Scenario: Design a class Shape and create two child classes Circle and
# Rectangle that implement the same method differently.
from math import pi
def p12():
    class Shape:
        @abstractmethod
        def getArea(self):
            pass
        
    class Circle(Shape):
        def __init__(self, r):
            self.r = r
        
        def getArea(self):
            return pi * (self.r ** 2)
    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w = w
            self.h = h
        
        def getArea(self):
            return 2 * (self.w + self.h)
        
# 13. Scenario: Create a base class Animal and multiple child classes to
# demonstrate hierarchical inheritance.
def p13():
    class Animal:
        def __init__(self, name):
            self.name = name
        
    class Dog(Animal):
        def __init__(self,name,breed):
            super().__init__(name)
            self.breed = breed
            
    class Cat(Animal):
        def __init__(self,name,breed):
            super().__init__(name)
            self.breed = breed
            
    class Bird(Animal):
        def __init__(self,name,type):
            super().__init__(name)
            self.type = type       
        
# 14. Scenario: Create a class Dog and another class Cat. Write a function that
# accepts both objects and calls the same method (Duck Typing).
def p14():
    class Dog:
        def method():
            print("this is a dog")
            
    class Cat:
        def method():
            print("this is a cat")
            
    def printMethod(Animal):
        Animal.method()
        
    dog = Dog
    cat = Cat
    printMethod(dog)
    printMethod(cat)
    
# 15. Scenario: Create a class Car with an inner class Engine. Demonstrate starting
# the engine and driving the car.
def p15():
    class Car:
        def __init__(self, engine):
            self.isRunning = False
            self.engine = self.Engine(engine)
            
        class Engine:
            def __init__(self, engine):
                self.engine = engine
                self.isStart = False
                
            def start(self):
                if self.isStart:
                    print("No need to start")
                else:
                    self.isStart = True
                print("Engine is running")

            def stop(self):
                if self.isStart:
                    self.isStart = False
                print("Engine is down")
                
            def getStatus(self):
                return self.isStart
            
        def startCar(self):
            self.engine.start()
            
        
            
        def drive(self):
            if self.engine.getStatus():
                self.isRunning = True
                print("Car is running now")
            else:
                print("Engine not started, start car first")
            
        def stop(self):
            if self.isRunning:
                self.isRunning = False
            print("Car has Stopped")
            
        def getStatus(self):
            return self.isRunning