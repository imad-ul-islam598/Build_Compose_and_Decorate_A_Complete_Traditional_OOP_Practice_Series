# Using cls
# _____________________________ Assignment 2 _____________________________
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

print("\n\t_____________________________ OUTPUT _____________________________")
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"\n Number of objects created: {cls.count}")

# Create instances of the Counter class
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

# Call the display_count method to print the count
Counter.display_count()