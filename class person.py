class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
        
    def display(self):
        print(f"Name: {self.Name}, Age: {self.Age}")
        
person1 = Person("Kato",22)
person2 = Person("Sam",20)

person1.display()
person2.display()

class Student(Person):
    def __init__(self, Name, Age, Accessnumber):
        super().__init__(Name, Age)
        self.Accessnumber = Accessnumber
        
    def display_info(self):
        super().display()
        print(f"Access Number: {self.Accessnumber}")
        
student1 = Student("Ronald", 23, "B23430")

student1.display_info()
