from contacts import Contacts
from addressbook import AddressBook
import validation

print("\nWelcome to Address Book Program!")

if __name__ == "__main__":
    address_book = AddressBook()
    
    while True:
        print("\n----Address Book Menu----")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit contact")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            try:
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
            except Exception as e:
                print("\nInvalid Input. Please try again.")
                continue
            validated_data = validation.validate_user_data(user_data)

            if validated_data:
                contact = Contacts(**validated_data)
                address_book.add_contact(contact)
            else:
                print("\n Contact not added due to errors. \n")
        elif choice == "2":
            address_book.print_address()
        elif choice == "3":
            search_name = input("\nEnter the Full Name of the contact to edit: ").strip().lower()
            address_book.edit_contact(search_name)
        elif choice == "4":
            break
        else:
            print("\nInvalid Choice. Please try again.")
            continue

