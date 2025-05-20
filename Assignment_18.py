# Property Decorators: @property, @setter, and @deleter
# _____________________________ Assignment 18 _____________________________
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

print("\n\t_____________________________ OUTPUT _____________________________")
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price
        print("\n Price deleted.")    

# Create an instance of the Product class
product = Product(100)

# Get the price using the @property decorator
print(f"\n Product Price:", product.price)

# Update the price using the @price.setter decorator
product.price = 200
print(f"\n Product Price:", product.price)

# Delete the price using the @price.deleter decorator
del product.price

# In the above code, we have created a Product class with a private attribute _price.
# We use the @property decorator to create a getter method for the price attribute, allowing us to access it as a property.
# We use the @price.setter decorator to create a setter method for the price attribute, allowing us to update it.
# We use the @price.deleter decorator to create a deleter method for the price attribute, allowing us to delete it.
# We create an instance of the Product class and use the getter method to access the price.
# We update the price using the setter method and delete it using the deleter method.
# This demonstrates how property decorators can be used to create getter, setter, and deleter methods for class attributes.
# Property decorators are a powerful feature in Python that allows for better encapsulation and control over class attributes.