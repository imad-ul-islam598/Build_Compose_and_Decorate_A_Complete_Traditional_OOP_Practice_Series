# Function Decorators
# _____________________________ Assignment 16 _____________________________
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

print("\n\t_____________________________ OUTPUT _____________________________")
def log_function_call(func):
    def wrapper():
        print("\n Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print(" Hello, World!")

say_hello()

# In the above code, we have created a decorator function log_function_call that prints "Function is being called" before executing the decorated function.
# The decorator takes a function as an argument and returns a wrapper function that prints the message and then calls the original function.
# We apply the decorator to the say_hello() function using the @log_function_call syntax.
# When we call the say_hello() function, the decorator function is executed first and prints the message before calling the original function.
# This demonstrates how function decorators can be used to modify the behavior of functions in a reusable and flexible way.
# Decorators are a powerful feature in Python that allows for better organization and separation of concerns in the code.
# They allow for better code reuse and flexibility by allowing functions to be modified or extended without changing their original implementation.