#In multilevel inheritance, a class inherits from a child class, forming a chain of inheritance. Here's an example in Python to demonstrate multilevel inheritance:


# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Intermediate class (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work_details(self):
        return f"I am {self.name}, my Employee ID is {self.employee_id}."

# Derived class (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def manager_details(self):
        return f"I am {self.name}, managing the {self.department} department."

# Create an object of the derived class
manager = Manager("Rohit", 30, "E123", "IT")

# Access methods from all levels of inheritance
print(manager.details())          # Output: My name is Rohit and I am 30 years old.
print(manager.work_details())     # Output: I am Rohit, my Employee ID is E123.
print(manager.manager_details())  # Output: I am Rohit, managing the IT department.
