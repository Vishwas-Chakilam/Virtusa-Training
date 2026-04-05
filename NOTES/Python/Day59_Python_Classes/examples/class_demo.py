class Student:
    # Class Attribute
    university = "Virtusa Academy"

    def __init__(self, name, id_number):
        # Instance Attributes
        self.name = name
        self.id = id_number

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Uni: {Student.university}")

s1 = Student("John", 101)
s2 = Student("Jane", 102)

s1.display()
s2.display()