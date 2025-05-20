# Aggregation
# _____________________________ Assignment 14 _____________________________
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

print("\n\t_____________________________ OUTPUT _____________________________")
class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Employee class
employee = Employee("IMAD UL ISLAM", 18)
# Create an instance of the Department class with a reference to the Employee object
department = Department("Physics", [employee])
# Print department and employee details
print(f"\n Department: {department.name}")
print(f" Employees: {department.employees[0].name}, {department.employees[0].age}")


# In the above code, we have created two classes: Department and Employee.
# The Employee class has an instance variable name and age.
# The Department class has an instance variable name and employees, which is a list of Employee objects.
# We create an instance of the Employee class and pass it to the Department class during initialization.
# This demonstrates how to use aggregation to create complex objects by combining simpler objects.
# Aggregation is a design pattern that allows objects to be composed of other objects.
# In this case, the Department object contains a reference to an Employee object that exists independently of it.
# This allows for better organization and separation of concerns in the code.
# Aggregation is a powerful concept in object-oriented programming that allows for better organization and separation of concerns in the code.
# It allows for better code reuse and flexibility by allowing objects to be composed of other objects.
# Aggregation is often preferred over inheritance in many cases because it allows for better code reuse and flexibility.
# This is useful for creating complex objects that are made up of simpler objects.