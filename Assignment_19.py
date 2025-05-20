# callable() and __call__()
# _____________________________ Assignment 19 _____________________________
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

print("\n\t_____________________________ OUTPUT _____________________________")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance of the Multiplier class
multiplier = Multiplier(10)

# Test the callable() function
print(f"\n Is multiplier callable? {callable(multiplier)}")
# Call the object like a function
result = multiplier(5)
print(f" Result: {result}")

# In the above code, we have created a Multiplier class with an __init__() method to set a factor.
# We define a __call__() method that multiplies an input by the factor.
# We create an instance of the Multiplier class and test it with the callable() function.
# We call the object like a function and store the result in a variable.
# This demonstrates how the __call__() method can be used to make an object callable like a function.
# The __call__() method allows us to define custom behavior for when an object is called like a function.
# This is useful for creating objects that behave like functions and can be used in a functional programming style.
# The callable() function is used to check if an object is callable, meaning it can be called like a function.
# This is useful for checking if an object can be called like a function before calling it.