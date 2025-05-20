# The super() Function
# _____________________________ Assignment 8 _____________________________
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

print("\n\t_____________________________ OUTPUT _____________________________")
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Create an instance of the Teacher class
teacher = Teacher("IMAD UL ISLAM", "Python Programming")
# Call the display method to print teacher details
print(f"\n Name: {teacher.name} \n Subject: {teacher.subject}")