class Employee:
    company_name = 'Virtusa'  # Class attribute
    
    def __init__(self, name, id):
        self.name = name          # Instance attribute
        self.id = id
        
    def display(self):
        print(f'[{Employee.company_name}] {self.id}: {self.name}')

emp1 = Employee('Alice', 101)
emp1.display()