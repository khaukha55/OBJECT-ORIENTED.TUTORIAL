class Reg_no:
    def __init__(Self, Name, Programme, Age, Registration_number):
        Self.Name = Name
        Self.Programme = Programme
        Self.Age = Age
        Self.Registration_number = Registration_number
    
    def display(self):
        print(f"Name:{self.Name}")
        print(f"Programme:{self.Programme}")
        print(f"Age{self.Age}")
        print(f"Registration_number:{self.Registration_number}")
        
Registration_number=input("Enter Your Registration_number: ")

student1 = Reg_no("Khaukha Ronald", "BSIT", 20, Registration_number)
student1.display()
        