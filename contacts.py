class Contacts:
    print("Welcome to Address Book Program")
    def __init__(self,fname,lname,address,city,state,zip,phonenum,email):
        self.fname = fname
        self.lname = lname
        self.phonenum = phonenum
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip
        self.email = email

    def __str__(self):
        return self.fname + " " + self.lname + " " + self.address + " " + self.city + " " + self.state + " " + self.zip_code + " " + self.phonenum + " " + self.email + "\n"
