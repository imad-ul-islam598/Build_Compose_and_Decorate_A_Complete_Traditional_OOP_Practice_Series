# Public Variables and Methods
# _____________________________ Assignment 3 _____________________________
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

print("\n\t_____________________________ OUTPUT _____________________________")
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"\n The {self.brand} car has started.")

# Create an instance of the Car class
car1 = Car("BMW")

# Access the public variable and method from outside the class
print(f"\n Brand: {car1.brand}")
car1.start()