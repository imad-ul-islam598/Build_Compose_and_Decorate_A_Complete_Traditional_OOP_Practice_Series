# Constructors and Destructors
# _____________________________ Assignment 6 _____________________________
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

print("\n\t_____________________________ OUTPUT _____________________________")
class Logger:
    def __init__(self):
        print("\n Logger object created.")

    def __del__(self):
        print("\n Logger object destroyed.")

# Create an instance of the Logger class
logger1 = Logger()

# Destroy the instance
del logger1