# Composition
# _____________________________ Assignment 13 _____________________________
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

print("\n\t_____________________________ OUTPUT _____________________________")
class Engine:
    def start(self):
        print("\n Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

# Create an instance of the Engine class
engine = Engine()
# Create an instance of the Car class with the Engine object
car = Car(engine)
# Call the start_car() method of the Car class to start the engine
car.start_car()

# In the above code, we have created two classes: Engine and Car.
# The Engine class has a method start() that prints a message when the engine is started.
# The Car class has an instance variable engine that is initialized with an Engine object during initialization.
# The start_car() method of the Car class calls the start() method of the Engine class to start the engine.
# We create an instance of the Engine class and pass it to the Car class during initialization.
# We call the start_car() method of the Car class to start the engine.
# This demonstrates how to use composition to create complex objects by combining simpler objects.
# Composition is a design pattern that allows objects to be composed of other objects.
# In this case, the Car object is composed of an Engine object.
# This allows for better organization and separation of concerns in the code.
# Composition is a powerful concept in object-oriented programming that allows for better organization and separation of concerns in the code.
# It allows for better code reuse and flexibility by allowing objects to be composed of other objects.
# This is useful for creating complex objects that are made up of simpler objects.
# Composition is often preferred over inheritance in many cases because it allows for better code reuse and flexibility.