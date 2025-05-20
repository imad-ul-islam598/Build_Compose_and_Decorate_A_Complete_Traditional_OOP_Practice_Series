# Method Resolution Order (MRO) and Diamond Inheritance
# _____________________________ Assignment 15 _____________________________
# Create four classes:
# ✔ A with a method show(),
# ✔ B and C that inherit from A and override show(),
# ✔ D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

print("\n\t_____________________________ OUTPUT _____________________________")
class A:
    def show(self):
        print("\n Class A")

class B(A):
    def show(self):
        print("\n Class B")

class C(A):
    def show(self):
        print("\n Class C")

class D(B, C):
    pass

d = D()
d.show()

# In the above code, we have created four classes: A, B, C, and D.
# The A class has a method show() that prints "Class A".
# The B and C classes inherit from A and override the show() method to print "Class B" and "Class C" respectively.
# The D class inherits from both B and C.
# We create an instance of the D class and call the show() method to observe the method resolution order (MRO).
# The MRO determines the order in which methods are resolved in the case of multiple inheritance.
# In this case, the MRO for class D is D -> B -> C -> A.
# This means that when we call the show() method on the D object, it will first look for the method in class D, then in class B, and finally in class A.
# This demonstrates how method resolution order (MRO) works in Python and how it affects the behavior of classes with multiple inheritance.
# The MRO is determined by the C3 linearization algorithm, which ensures that the order of method resolution is consistent and predictable.
# The MRO can be viewed using the mro() method or the __mro__ attribute of the class.
# This is useful for understanding how methods are resolved in the case of multiple inheritance and how it affects the behavior of classes.
# The MRO is an important concept in object-oriented programming that allows for better organization and separation of concerns in the code.
# It allows for better code reuse and flexibility by allowing objects to be composed of other objects.