class Contacts:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return (f"{self.fname} {self.lname}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.phonenum}, {self.email}\n")
