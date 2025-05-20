# Make a Custom Class Iterable
# _____________________________ Assignment 21 _____________________________
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

print("\n\t_____________________________ OUTPUT _____________________________")
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration
# Create an instance of the Countdown class
countdown = Countdown(5)

# Iterate over the countdown object using a for-loop
for number in countdown:
    print(f"\n Number: {number}")

# In the above code, we have created a Countdown class that takes a start number.
# We implement the __iter__() and __next__() methods to make the object iterable in a for-loop, counting down to 0.
# We create an instance of the Countdown class and iterate over it using a for-loop.
# This demonstrates how to create a custom iterable class in Python.
# The __iter__() method returns the iterator object itself, and the __next__() method returns the next value in the iteration.
# When the countdown reaches -1, we raise a StopIteration exception to signal the end of the iteration.
# This allows us to create custom iterable objects that can be used in a for-loop or with other iterable functions.
# This is useful for creating custom data structures that can be iterated over in a consistent and predictable way.x``