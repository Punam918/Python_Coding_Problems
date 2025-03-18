# Pass by value
def modify_value(x):
    x = 10  # This rebinds x to a new object, so the original object remains unchanged.

a = 5
modify_value(a)
print(a)  # Output will be 5, as the original value of 'a' is not modified.

'''
When you pass immutable objects (like int, float, str, tuple) to a function, it behaves like pass by value. 
This means any changes made to the argument inside the function will not affect the original object.
'''

#pass by reference
def modify_list(lst):
    lst.append(4)  # This modifies the original list, since lists are mutable.

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output will be [1, 2, 3, 4], as the original list is modified.

'''
When you pass mutable objects (like list, dict, set) to a function,
Python passes the reference to the object, not a copy. 
This means changes made to the object inside the function will affect the original object outside 
the function.
'''