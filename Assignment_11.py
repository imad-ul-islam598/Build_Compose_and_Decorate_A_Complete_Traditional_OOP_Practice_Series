# Class Methods
# _____________________________ Assignment 11 _____________________________
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

print("\n\t_____________________________ OUTPUT _____________________________")
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"\n Total books: {cls.total_books}")
# Create instances of the Book class
book1 = Book()
book2 = Book()
book3 = Book()
# Call the increment_book_count() method to increase the count
book1.increment_book_count()
book2.increment_book_count()
book3.increment_book_count()

# In the above code, we have created a Book class with a class variable total_books.
# The increment_book_count() method increases the count of total_books by 1.
# We create three instances of the Book class and call the increment_book_count() method to increase the count.
# This demonstrates how to use class methods to access class variables and perform actions related to the class.
# Class methods are used to access and modify class variables, while instance methods are used to access and modify instance variables.