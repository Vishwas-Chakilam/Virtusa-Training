class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def assign_task(self, task):
        return f"{self.name} assigned task '{task}' to the {self.department} team."

m = Manager("Eve", 120000, "Engineering")
print(m.assign_task("Refactor backend services"))