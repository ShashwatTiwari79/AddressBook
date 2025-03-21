from address_book_main import AddressBookMain
from contacts import Contacts
from addressbook import AddressBook
import validation
import os


def manage_contacts(book):
    os.makedirs("data/csv", exist_ok=True)  
    os.makedirs("data/json", exist_ok=True)  
    
    while True:
        print("\n----Address Book Menu----")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit contact")
        print("4. Delete Contact")
        print("5. Sorting by name")
        print("6. Sorting by city , state or zip")
        print("7. Save to file")
        print("8. Load from file")
        print("9. Exit")
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
                book.add_contact(contact)
            else:
                print("\n Contact not added due to errors. \n")
        elif choice == "2":
            book.print_address()
        elif choice == "3":
            search_name = input("\nEnter the Full Name of the contact to edit: ").strip().lower()
            book.edit_contact(search_name)
        elif choice == "4":
            search_name = input("\nEnter the Full Name of the contact to delete: ").strip().lower()
            book.delete_contact(search_name)
        elif choice == "5":
            book.sort_contacts()
        elif choice == "6":
            print("\nSort by:")
            print("1. City")
            print("2. State")
            print("3. Zip Code")
            choice = input("Enter your choice: ").strip()
            if choice in ["1", "2", "3"]:
                book.sort_person_city_state_zip(int(choice))
        elif choice == "7":
            book.save_to_file()
        elif choice == "8":
            book.load_from_file()
        elif choice == "9":
            break
        else:
            print("\nInvalid Choice. Please try again.")
            continue
def main():
    print("\nWelcome to the Address Book System!")

    Mainbook = AddressBookMain()

    while True:
        print("\nOptions: ")
        print("1. Create Address Book")
        print("2. Select Address Books")
        print("3. Display Address Book")
        print("4. Delete Address Book")
        print("5. Search contact by city or state")
        print("6. View person by city or state")
        print("7. Count person by city or state")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
           name = input("Enter new Address Book name: ").strip()
           Mainbook.add_address_book(name)

        elif choice == "2":
            name = input("Enter the  Address Book to select: ").strip()
            book = Mainbook.select_address_book(name)

            if book:
                manage_contacts(book)

        elif choice == "3":
            Mainbook.display_address_books()

        elif choice  == "4":
            name = input("Enter the Address Book to delete: ").strip()
            Mainbook.delete_address_book(name)

        elif choice =="5":
            location = input("Enter the city or state to be searched: ").strip()
            Mainbook.search_person_city(location)
        elif choice == "6":
            Mainbook.view_person_city_state()
        elif choice == "7":
            Mainbook.view_person_city_state(False)
        elif choice == "8":
            exit("\nExiting Address Book System.")        
if __name__ == "__main__":
    main()