# Static Variables and Static Methods
# _____________________________ Assignment 5 _____________________________
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

print("\n\t_____________________________ OUTPUT _____________________________")
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
# Call the static method to add two numbers
result = MathUtils.add(5, 3)
print(f"\n Sum: {result}")