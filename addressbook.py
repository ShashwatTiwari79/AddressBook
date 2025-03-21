from contacts import Contacts

class AddressBook:
    def __init__(self,name):
        self.name = name
        self.contacts = {}
   
    def add_contact(self, contact_obj):
        for existing_contact in self.contacts.values():
            if (existing_contact.fname.lower() == contact_obj.fname.lower() and
                existing_contact.lname.lower() == contact_obj.lname.lower()):
                print("\nError: A contact with the same name already exists in this Address Book!")
                return
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
    def delete_contact(self, full_name):
        for phone, contact in self.contacts.items():
            if f"{contact.fname} {contact.lname}".strip().lower() == full_name.lower():
                del self.contacts[phone]
                print("\nContact Deleted Successfully!")
                
                return

        print("\nContact not found.")
    def sort_contacts(self):
        sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.fname)
        print("\nContacts sorted by First Name:")
        for contact in sorted_contacts:
            print(contact)
    def sort_person_city_state_zip(self,choice):
        if choice == 1:
            sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.city)
            print("\nContacts sorted by City:")
            for contact in sorted_contacts:
                print(contact)
        elif choice == 2:
            sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.state)
            print("\nContacts sorted by State:")
            for contact in sorted_contacts:
                print(contact)
        elif choice == 3:
            sorted_contacts = sorted(self.contacts.values(), key=lambda x: x.zip)
            print("\nContacts sorted by Zip Code:")
            for contact in sorted_contacts:
                print(contact)
        else:
            print("wrong choice")

    