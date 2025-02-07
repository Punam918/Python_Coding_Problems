'''Getters, Setters, Property Decorators.'''
# In Python, getters and setters are methods used to control access to class attributes. 
# They are often implemented using the property decorator.


'''without decorators getter and setters'''
" Here, get_age() acts as a getter and set_age() acts as a setter."
class Person:
    def __init__(self, name, age):
        self._name = name     
        self._age = age      

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be positive")

# Using the getter and setter
p = Person("Alice", 25)
print(p.get_age())  
p.set_age(30)       
print(p.get_age()) 



'''With Decorators'''
"Getters and Setters Using @property Decorator"
'''Instead of defining separate methods for getting and setting values,
Python provides the @property decorator, making the syntax more concise.'''

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):  # Getter
        return self._age

    @age.setter
    def age(self, new_age):  # Setter
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be positive")

p = Person("Bob", 28)
print(p.age)   # Calls the getter (Output: 28)
p.age = 35     # Calls the setter
print(p.age)   # Output: 35
