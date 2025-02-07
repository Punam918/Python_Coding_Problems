'''Object Method Vs Static Method'''
#Object Method (Instance Method)
'''Object methods are functions that are defined inside a class and take self as their first parameter,
referring to the instance of the class.
These methods can access and modify the instance's attributes.'''

class MyClass:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(f"Value: {self.value}")

obj = MyClass(10)
obj.show_value()  # This Calls the object method

'''Static methods are functions that belong to the class rather than any instance. 
They do not have access to self (the instance) or cls (the class).
Static methods are defined using the @staticmethod decorator.'''
class MyClass:
    @staticmethod
    def multiply(x, y):
        return x * y

result = MyClass.multiply(3, 4)  # Calls the static method without an instance
print(result)


