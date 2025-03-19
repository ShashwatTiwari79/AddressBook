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