'''You want to invoke a method in a parent class in place of a method that has been
overridden in a subclass. Explore mro.'''



# To invoke a method from a parent class instead of an overridden method in a subclass, 
# you can use the super() function in Python, which allows you to access the parent class's
# methods within the subclass, effectively "calling up" the method resolution order (MRO) to reach
# the desired parent method. 
# Key points about MRO and super():
# MRO (Method Resolution Order):
# This is the order in which Python searches for methods when a method is called on an object, starting from the class itself, then its parent class, and so on through the inheritance hierarchy. 

class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

    def bark(self):
        super().speak()
print(Dog.__mro__)
print(Animal.__mro__)
my_dog = Dog()
my_dog.bark() 
