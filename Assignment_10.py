# Instance Methods
# _____________________________ Assignment 10 _____________________________
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

print("\n\t_____________________________ OUTPUT _____________________________")
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"\n {self.name} says Woof! I am a {self.breed} dog.")

# Create an instance of the Dog class
dog = Dog("Buddy", "Golden Retriever")
# Call the bark method to print a message
dog.bark()

# In the above code, we have created a Dog class with instance variables name and breed.
# The bark() method prints a message including the dog's name and breed.
# We create an instance of the Dog class and call the bark() method to print the message.
# This demonstrates how to use instance methods to access instance variables and perform actions related to the object.