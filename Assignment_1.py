# Using self
# _____________________________ Assignment 1 _____________________________
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

print("\n\t_____________________________ OUTPUT _____________________________")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"\n Name: {self.name} \n Marks: {self.marks}")    
# Create an instance of the Student class
student1 = Student("IMAD UL ISLAM", 95)
# Call the display method to print student details
student1.display()