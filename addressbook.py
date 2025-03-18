from contacts import Contacts

class AddressBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, contact_obj):
        if contact_obj.phonenum in self.contacts:
            print("\nContact with this phone number already exists!")
        else:
            self.contacts[contact_obj.phonenum] = contact_obj
            print("\nContact Added Successfully!")

    def print_address(self):
        if not self.contacts:
            print("\nAddress Book is empty!")
        else:
            print("\nAddress Book:")
            for contact in self.contacts.values():
                print(contact)
    def edit_contact(self,full_name):
        
        
        for phone, contact in self.contacts.items():
            if f"{contact.fname} {contact.lname}".strip().lower() == full_name.lower():
                print(f"\nEditing Contact: {contact}")

                new_fname = input("Enter new First Name (leave blank to keep current): ") or contact.fname
                new_lname = input("Enter new Last Name (leave blank to keep current): ") or contact.lname
                new_address = input("Enter new Address (leave blank to keep current): ") or contact.address
                new_city = input("Enter new City (leave blank to keep current): ") or contact.city
                new_state = input("Enter new State (leave blank to keep current): ") or contact.state
                new_zip = input("Enter new Zip Code (leave blank to keep current): ") or contact.zip
                new_phone = input("Enter new Phone Number (leave blank to keep current): ") or contact.phonenum
                new_email = input("Enter new Email (leave blank to keep current): ") or contact.email
                if new_phone != contact.phonenum:
                    del self.contacts[contact.phonenum]
                    self.contacts[new_phone] = contact

                contact.fname = new_fname
                contact.lname = new_lname
                contact.address = new_address
                contact.city = new_city
                contact.state = new_state
                contact.zip = new_zip
                contact.phonenum = new_phone
                contact.email = new_email

                print("\nContact updated successfully!")
                return

        print("\nContact not found.")
    