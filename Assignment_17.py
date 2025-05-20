# Class Decorators
# _____________________________ Assignment 17 _____________________________
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

print("\n\t_____________________________ OUTPUT _____________________________")
def add_greeting(cls):
    def greet(self):
        return "\n Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("IMAD UL ISLAM")
# Call the greet method to see the modified behavior
print(p.greet())

# In the above code, we have created a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
# The decorator takes a class as an argument and adds the greet() method to it.
# We apply the decorator to the Person class using the @add_greeting syntax.
# When we create an instance of the Person class, we can call the greet() method to see the modified behavior.
# This demonstrates how class decorators can be used to modify the behavior of classes in a reusable and flexible way.
# Class decorators are a powerful feature in Python that allows for better organization and separation of concerns in the code.
# They allow for better code reuse and flexibility by allowing classes to be modified or extended without changing their original implementation.
# Class decorators are similar to function decorators but are applied to classes instead of functions.