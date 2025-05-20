# Static Methods
# _____________________________ Assignment 12 _____________________________
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

print("\n\t_____________________________ OUTPUT _____________________________")
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
# Call the static method to convert Celsius to Fahrenheit
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"\n Fahrenheit: {fahrenheit}")

# In the above code, we have created a TemperatureConverter class with a static method celsius_to_fahrenheit(c).
# The celsius_to_fahrenheit() method takes a Celsius value as input and returns the corresponding Fahrenheit value using the formula (C * 9/5) + 32.
# We call the static method to convert 25 degrees Celsius to Fahrenheit and print the result.
# This demonstrates how to use static methods to perform calculations or operations that do not require access to instance or class variables.
# Static methods are used for utility functions that are related to the class but do not require access to instance or class variables.
# Static methods are defined using the @staticmethod decorator and can be called directly on the class without creating an instance.
# This is useful for creating utility functions that are related to the class but do not require access to instance or class variables.