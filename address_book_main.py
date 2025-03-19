from collections import defaultdict
from addressbook import AddressBook


class AddressBookMain:
    
    def __init__(self):
        self.addressbook = {}

    def add_address_book(self ,name):
       
        if name in self.addressbook:
            print(f"\n'{name}' Address Book already exists.")
        else:
            self.addressbook[name] = AddressBook(name)
            print(f"\n'{name}' Address Book created successfully!")

    def display_address_books(self):
        
        if not self.addressbook:
            print("\nNo Address Books to display.")
        else:
            print(f"\nAddress Books:")
            for name in self.addressbook.keys():
                print(f"\n{name}")

    def select_address_book(self , name):
       
        if name in self.addressbook:
            return self.addressbook[name]
        print(f"\n'{name}' Address Book not found!")
        return None

    def delete_address_book(self , name):
       
        if name in self.addressbook:
            del self.addressbook[name]
            print(f"\n'{name}' Address Book deleted successfully!")
        else:
            print(f"\n'{name}' Address Book not found!")
    def search_person_city(self,location):
        found_contacts = []
        for book_name,address_book in self.addressbook.items():
            for contact in address_book.contacts.values():
                if contact.city.lower() == location.lower() or contact.state.lower() == location.lower():
                    found_contacts.append((book_name,contact))
        if found_contacts:
            print(f"\nContacts found in Address Books:")
            for book_name, contact in found_contacts:
                print(f"\nAddress Book: {book_name}")
                print(f"contacts:- {contact}\n")
        else:
            print("\nNo contacts found in the specified location.")
    def view_person_city_state(self):
        city_loc = defaultdict(list)
        state_loc = defaultdict(list)
        for book_name,address_book in self.addressbook.items():
            for contact in address_book.contacts.values():
                city_loc[contact.city].append(f"[{book_name}]{contact.fname} {contact.lname} {contact.phonenum} {contact.email}")
                state_loc[contact.state].append(f"[{book_name}]{contact.fname} {contact.lname} {contact.phonenum} {contact.email}")
        print("\nContacts by City:")
        for city, contacts in city_loc.items():
            print(f"\nCity: {city}")
            for contact in contacts:
                print(contact)
        print("\nContacts by State:")
        for state, contacts in state_loc.items():
            print(f"\nState: {state}")
            for contact in contacts:
                print(contact)
        