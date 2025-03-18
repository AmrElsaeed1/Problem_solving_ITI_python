# Base Class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived Class: Employee (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  # Call Person's __init__
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        super().display_info()  # Call Person's display_info
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


# Derived Class: Manager (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)  # Call Employee's __init__
        self.department = department

    def display_info(self):
        super().display_info()  # Call Employee's display_info
        print(f"Department: {self.department}")


manager = Manager(name="John Doe", age=40, employee_id=101, salary=80000, department="IT")

# Display manager's information
manager.display_info()