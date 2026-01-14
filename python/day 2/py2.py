from fractions import Fraction
import math

def prog_1():
    a = input()
    return (a <= 100)

def prog_2():
    i = 1
    flt = 1.1
    print("type of ", i, "is ", type(i))
    print("type of ", flt, "is ", type(flt))
    
def statement():
    print(complex(4,5))
    
def code():
    print(0b1101011)
    
def prog_3():
    print(isinstance(4, int))

def code_2():
    print(Fraction('1.5'))

def prog_4():
    print(math.sqrt(9))

def code_3():
    a = [[1,2],[2,3],[4,5]]
    print(a[2][1])

def code_4():
    a = ['p','r','o','g','r','a','m']
    a = a[2:5]
    print(a)
    
def code_5():
    tp =(['a', 'b', 'c'],[0, 2, 3, 4])
    print(tp)
    tp[1][1] = 5 
    print(tp)