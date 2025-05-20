# Class Variables and Class Methods
# _____________________________ Assignment 4 _____________________________
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

print("\n\t_____________________________ OUTPUT _____________________________")
class Bank:
    bank_name = "Mezan Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"\n Bank name has changed to: {cls.bank_name}\n")
# Create instances of the Bank class
bank1 = Bank()
bank2 = Bank()

# Call the change_bank_name method to change the bank name
Bank.change_bank_name(" Habib Bank")
# Show that the change affects all instances
print(f" Bank 1 Name: {bank1.bank_name}")
print(f" Bank 2 Name: {bank2.bank_name}")