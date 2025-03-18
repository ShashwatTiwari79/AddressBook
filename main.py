from contacts import Contacts
from addressbook import AddressBook
import validation

print("\nWelcome to Address Book Program!")

if __name__ == "__main__":
    address_book = AddressBook()
    
    while True:
        print("\nEnter Contact Details:")
        user_data = {
            "fname": input("Enter First Name: "),
            "lname": input("Enter Last Name: "),
            "address": input("Enter Address: "),
            "city": input("Enter City: "),
            "state": input("Enter State: "),
            "zip": input("Enter Zip Code: "),
            "phonenum": input("Enter Phone Number: "),
            "email": input("Enter Email: ")
        }

        validated_data = validation.validate_user_data(user_data)

        if validated_data:
            contact = Contacts(**validated_data)
            address_book.add_contact(contact)
        else:
            print("\n Contact not added due to errors. \n")

        choice = input("\nDo you want to add another contact? (yes/no): ").strip().lower()
        if choice == "no":
            break

    # Display all valid contacts
    address_book.print_address()
