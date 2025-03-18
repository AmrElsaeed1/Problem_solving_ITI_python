class Person:
    def __init__(self, name, money=0, mood="neutral", health_rate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        return self.mood

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50
        else:
            # Handle edge case of 0 or negative meals
            self.health_rate = max(0, self.health_rate - 10)
        return self.health_rate

    def buy(self, items):
        cost = items * 10  # Each item costs 10 L.E.
        if self.money >= cost:
            self.money -= cost
            return "Done"
        else:
            return "Not enough money"  # Not enough money


class Car:
    def __init__(self,name,fuel_rate=100,velocity=0):
        self.name=name
        self._fuel_rate=fuel_rate
        self._velocity=velocity



    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            self._fuel_rate = min(max(0, value), 100)  # Constrain between 0 and 100

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            self._velocity = min(max(0, value), 200)  # Constrain between 0 and 200

    def run(self,distance,velocity):
        self.velocity=velocity
        max_distance=self._fuel_rate
        if distance <= max_distance:
            self._fuel_rate-=distance
            remaining_distance=0
            print(f"Driving {max_distance} units at velocity {velocity}")

        else:
            remaining_distance=distance-max_distance
            self._fuel_rate=0
            print(f"Driving {max_distance} units at velocity {velocity}")

        self.stop(remaining_distance)

    def stop(self, remaining_distance=0):
        self.velocity = 0
        if remaining_distance == 0:
            print("You have arrived at your destination!")
        else:
            print(f"You have stopped with {remaining_distance} units remaining to your destination.")



class Employee(Person):
    def __init__(self, name, id, email, salary, distance_to_work, car=None, money=0, mood="neutral", health_rate=100):
        super().__init__(name, money, mood, health_rate)
        self.id = id
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work
        self.car = car

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        return self.mood


    def drive(self,distance,veloicty=60):
        if self.car:
            self.car.run(distance,veloicty)
        else:
            print("has no car")

    def refuel(self,gasamout=100):
        if self.car:
            self.car.fuel_rate+=gasamout
            print(f"new fuel rate {self.car.fuel_rate}")
        else:
            print("doesn't have a car")

    def send_mail(self, recipient, subject, body):
        print(f"Email sent from {self.email} to {recipient}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")


class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employees_num = num

    def get_all_employees(self):

        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None  # Return None if no employee is found

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1  # Increment the total number of employees
        print(f"{employee.name} has been hired.")

    def fire(self, emp_id):
        """Fire the employee with the given ID."""
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employees_num -= 1  # Decrement the total number of employees
            print(f"{emp.name} (ID: {emp_id}) has been fired.")
        else:
            print(f"No employee found with ID: {emp_id}.")

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} from {emp.name}'s salary. New salary: {emp.salary}.")
        else:
            print(f"No employee found with ID: {emp_id}.")

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward
            print(f"Rewarded {reward} to {emp.name}'s salary. New salary: {emp.salary}.")
        else:
            print(f"No employee found with ID: {emp_id}.")

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            target_hour = 9  # Assume the target hour to be at the office is 9 AM
            is_late = Office.calculate_lateness(target_hour, move_hour, emp.distance_to_work,
                                                emp.car.velocity if emp.car else 60)
            if is_late:
                self.deduct(emp_id, 10)
                print(f"{emp.name} is late. Deducted 10 from salary.")
            else:
                self.reward(emp_id, 10)
                print(f"{emp.name} is on time. Rewarded 10 to salary.")
        else:
            print(f"No employee found with ID: {emp_id}.")

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):

        if velocity == 0:
            return True  # Avoid division by zero
        travel_time = distance / velocity  # Time taken to reach the office
        arrival_hour = move_hour + travel_time
        return arrival_hour > target_hour



# Create a car
car = Car("Toyota", fuel_rate=50, velocity=60)

# Create employees
emp1 = Employee(name="Alice", id=1, email="alice@example.com", salary=5000, distance_to_work=30, car=car)
emp2 = Employee(name="Bob", id=2, email="bob@example.com", salary=6000, distance_to_work=40, car=None)

# Create an office
office = Office("Tech Office")

# Test Office methods
print("===== Office Methods =====")
office.hire(emp1)  # Hire Alice
office.hire(emp2)  # Hire Bob
print("All Employees:", [emp.name for emp in office.get_all_employees()])  # Get all employees
print("Employee with ID 1:", office.get_employee(1).name)  # Get employee by ID
office.check_lateness(1, move_hour=8)  # Check if Alice is late (move_hour = 8)
office.check_lateness(2, move_hour=7)  # Check if Bob is late (move_hour = 7)
office.deduct(1, 100)  # Deduct 100 from Alice's salary
office.reward(2, 200)  # Reward 200 to Bob's salary
office.fire(1)  # Fire Alice
print("Total Employees in all offices:", Office.employees_num)  # Print total employees

# Test Employee methods
print("\n===== Employee Methods =====")
emp1.work(8)  # Alice works for 8 hours
emp2.work(10)  # Bob works for 10 hours
emp1.drive(30, 60)  # Alice drives 30 units at 60 velocity
emp2.drive(40)  # Bob tries to drive but has no car
emp1.refuel(50)  # Alice refuels her car
emp2.refuel(50)  # Bob tries to refuel but has no car
emp1.send_mail("manager@example.com", "Report", "Here is my report.")  # Alice sends an email
emp2.send_mail("manager@example.com", "Issue", "I have an issue.")  # Bob sends an email

# Test Car methods
print("\n===== Car Methods =====")
car.run(30, 60)  # Drive the car for 30 units at 60 velocity
car.stop()  # Stop the car
car.fuel_rate = 120  # Try to set fuel rate to 120 (will be constrained to 100)
print("Fuel Rate:", car.fuel_rate)
car.velocity = 250  # Try to set velocity to 250 (will be constrained to 200)
print("Velocity:", car.velocity)

# Test Person methods
print("\n===== Person Methods =====")
emp1.sleep(7)  # Alice sleeps for 7 hours
emp2.sleep(5)  # Bob sleeps for 5 hours
emp1.eat(3)  # Alice eats 3 meals
emp2.eat(1)  # Bob eats 1 meal
print("Alice's Health Rate:", emp1.health_rate)
print("Bob's Health Rate:", emp2.health_rate)
emp1.buy(5)  # Alice buys 5 items
emp2.buy(3)  # Bob buys 3 items
print("Alice's Money:", emp1.money)
print("Bob's Money:", emp2.money)
