'''. Explore private, public and protected variables. Also explore objectmethod, static method and create
a questions yourself regarding these.'''
'''
In Python, the concept of private, public, and protected variables pertains to the accessibility of attributes and methods within and outside of a class.'''

#public variables
class MyClass:
    def __init__(self):
        self.public_var = 5 

obj = MyClass()
#it shows it can be accessed from outside the class
print(obj.public_var) 

#protected variables
#protected variables are meant to be accessed within class and subclass
#we use underscore but its just a convention not a actual access control method

class MyClass:
    def __init__(self):
        self._protected_var = 10 
obj = MyClass()
print(obj._protected_var)  

##private variables
#Private variables are meant to be accessible only within the class. 
# They are defined by using a double underscore (__) before the variable name. 
class MyClass:
    def __init__(self):
        self.__private_var = 20  # Private variable

obj = MyClass()
# print(obj.__private_var)  # Raises an AttributeError
print(obj._MyClass__private_var)  # Accessing using name mangling (not recommended)

class MyClass:
    def __init__(self):
        self.__private = 40
        self._protected = 50
        self.public = 30

    def display(self):
        print(self.__private)
        print(self._protected)
        print(self.public)

obj = MyClass()
print(obj._MyClass__private)
print(obj._protected)
print(obj.public)