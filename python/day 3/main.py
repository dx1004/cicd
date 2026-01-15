def Q1():
    # 1. create a tuple that contains an integer, a boolean,
    # a string, and a list. 
    a = (1, True, "a", [1,2,3,4])

def Q2():
    """ 2. Write a program to access and slice a tuple ('p','r','o','g','r','a','m','I','z') to extract:
    (a) elements from index 2 to 5
    (b) elements from the beginning to index -5
    (c) elements from index 5 to the end. """
    tp = ('p','r','o','g','r','a','m','I','z')
    a = tp[2:5]
    b = tp[:-5]
    c = tp[5:]

def Q3():
    # 3. Demonstrate tuple concatenation and repetition using two example tuples and explain the output.
    tp1 = (1,2,3)
    tp2 = (2,3,4)
    tpc = tp1 + tp2
    tpr = tp1 * 2
    # concat with +, repeat with *
    
def Q4():
    '''4. Given a tuple ('a','p','p','l','e'), write a program to find:
    (a) the count of 'p'
    (b) the index of 'l'.'''
    tp = ('a','p','p','l','e')
    print(tp.count('p')) # ans for a
    print(tp.index('l')) # ans for b

def Q5():
    '''5. Create a string and demonstrate string
    immutability by attempting an invalid modification
    and then deleting the string.'''
    s = "this is a string"
    # line below will fail due to 
    # TypeError: 'str' object does not support item assignment
    # s[5] = 5
    del(s) # this deletes the string
    
def Q6():
    # 6. Write a program using escape sequences and raw
    # strings to show the difference in output.
    print("this is a str without esc seq") 
    print("this is a \n str with escape seq") # \n print as newline
    
def Q7():
    # 7. Create a set with duplicate elements and
    # demonstrate how Python handles duplicates. Then
    # perform union and intersection on two sets.    
    s1 = {1,2,3,3,3,4,5} # duplicated value with be removed automatically for set 
    s2 = {4,6,7,8}
    print(s1|s2) # this performs the union of 2 sets
    print(s1+s2) # this performs the intersection on two sets
    
def Q8():
    # 8. Write a program to add and remove elements from
    # a set using add(), update(), discard(), and remove().
    aset = {1,2,3,4,5,6,7}
    aset.add(8) # add 8 at the end of the set
    aset.update({"this", "that"}) # add this set to the end of aset
    aset.discard(3) # delete 3 from the set and if 3 does not exist it will not raise err
    aset.remove(2) # delete 2 from the set
    
def Q9():
    # 9. Create a dictionary with student names as keys
    # and marks as values. Add a new entry, modify an
    # existing one, and remove one key using pop().
    dic = {"John": 90, "James": 85, "Peter":77}
    dic["Johnson"] = 87
    dic["John"] = 89
    dic.pop("Peter")
    
def Q10():
    # 10. Create a nested dictionary representing two
    # people with names and ages. Write a program to
    # iterate and print all details.
    ndict = {
         "John": {"age": 20},
         "Ben": {"age": 29}
    }
    for name, info in ndict.items():
        print(f"Name: {name}")
        for key, value in info.items():
            print(f"    {key}:{value}")
            
def Q11():
    # 11. Explain why tuples can be used as dictionary keys but lists cannot, with a
    # code example.
    # Tuples work as keys because they are hashable
    location_data = {(40.7128, -74.0060): "New York"}
    print(location_data[(40.7128, -74.0060)])  # Output: New York

    # Lists fail because they are "unhashable"
    try:
        invalid_dict = {[1, 2]: "Invalid"}
    except TypeError as e:
        print(f"Error: {e}")  # Output: Error: unhashable type: 'list'

def Q12():
    # 12. What happens when you assign the same mutable object to two different
    # variables? Demonstrate with a list example.
    # Create a list and assign it to 'list_a'
    list_a = [1, 2, 3]

    # Assign list_a to list_b (both now point to the same object)
    list_b = list_a

    # Modify list_b
    list_b.append(4)

    # Both variables reflect the change
    print(f"list_a: {list_a}") # Output: [1, 2, 3, 4]
    print(f"list_b: {list_b}") # Output: [1, 2, 3, 4]

    # Verification: check if they are the same object in memory
    print(list_a is list_b)     # Output: True

def Q13():
    # 13. Explain the difference between '==' and 'is' using variables and immutable
    # data types.
    # Strings (Immutable)
    str1 = "hello"
    str2 = "hello"

    print(str1 == str2)  # True (Values are identical)
    print(str1 is str2)  # True (Python reused the same object in memory)

    # Larger Integers / Manual Creation
    a = 1000
    b = 1000

    print(a == b)        # True (Values are identical)
    print(a is b)        # False (Usually different objects in memory depending on the environment)

def Q14():
    # 14. How does Python handle variable reassignment for immutable vs
    # mutable data types?
    x = 10      # 'x' points to an integer object 10
    x = x + 1   # A new integer object 11 is created; 'x' now points to it
    list1 = [1, 2]  # 'list1' points to object A
    list1 = [3, 4]  # 'list1' now points to a brand new object B; object A is discarded

def Q15():
    # 15. Given a dictionary containing numerical values, write a program to
    # calculate the sum of all values.
    marks = {"Math": 85, "Science": 90, "English": 78}
    
    # Get the sum of all values
    total_sum = sum(marks.values())
    
    print(f"Total Sum: {total_sum}") 
    # Output: Total Sum: 253
