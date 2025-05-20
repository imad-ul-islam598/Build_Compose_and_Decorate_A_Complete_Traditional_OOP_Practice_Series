# Access Modifiers: Public, Private, and Protected
# _____________________________ Assignment 7 _____________________________
# Create a class Employee with:
# ✔ a public variable name,
# ✔ a protected variable _salary, and
# ✔ a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

print("\n\t_____________________________ OUTPUT _____________________________")
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

# Create an instance of the Employee class
employee = Employee("John Doe", 50000, "123-45-6789")

# Access the public variable
print(f"\n Name: {employee.name}")

# Access the protected variable
print(f" Salary: {employee._salary}")

# Access the private variable
try:
    print(f" SSN: {employee.__ssn}")  # This will raise an AttributeError
except AttributeError as e:
    print(f" Error: {e}")
# Access the private variable using name mangling
print(f" SSN (using name mangling): {employee._Employee__ssn}")

# In Python, private variables are not truly private. They can be accessed using name mangling.
# However, it is a convention to treat variables prefixed with double underscores as private.
# In this case, the private variable __ssn can be accessed using the name mangling convention _Employee__ssn.
# In summary:
# - Public variables can be accessed directly.
# - Protected variables can be accessed directly but are intended for internal use.
# - Private variables cannot be accessed directly and raise an AttributeError.
# However, they can be accessed using name mangling.
# This is a convention in Python to indicate that the variable is intended to be private.
# In practice, it is recommended to use public and protected variables for better encapsulation and to avoid accessing private variables directly.