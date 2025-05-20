# Creating a Custom Exception
# _____________________________ Assignment 20 _____________________________
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

print("\n\t_____________________________ OUTPUT _____________________________")
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print(f"\n Age is valid: {age}")

try:
    check_age(17)
except InvalidAgeError as e:
    print(f"\n {e}")

# In the above code, we have created a custom exception InvalidAgeError that inherits from the built-in Exception class.
# We define a function check_age(age) that raises this exception if the age is less than 18.
# We use a try...except block to handle the exception when calling the check_age() function with an age of 17.
# This demonstrates how to create and handle custom exceptions in Python.
# Custom exceptions allow us to define our own error types and handle them in a specific way.
# This is useful for creating more meaningful error messages and handling specific error conditions in our code.