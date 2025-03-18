# Employee Management System

This project demonstrates a simple **Employee Management System** using Python classes. It includes four main classes: `Person`, `Car`, `Employee`, and `Office`. The system allows you to manage employees, their attributes, and their interactions with cars and the office.

---

## Classes Overview

### 1. **Person Class**
   - Represents a generic person with attributes:
     - `name`: Name of the person.
     - `money`: Amount of money the person has.
     - `mood`: Current mood of the person (e.g., happy, tired, lazy).
     - `health_rate`: Health rate of the person (0-100%).
   - **Methods**:
     - `sleep(hours)`: Updates the mood based on hours of sleep.
     - `eat(meals)`: Updates the health rate based on the number of meals.
     - `buy(items)`: Deducts money based on the number of items bought.

### 2. **Car Class**
   - Represents a car with attributes:
     - `name`: Name of the car.
     - `fuel_rate`: Fuel level of the car (0-100%).
     - `velocity`: Current speed of the car (0-200 km/h).
   - **Methods**:
     - `run(distance, velocity)`: Simulates driving the car for a given distance and velocity.
     - `stop(remaining_distance)`: Stops the car and displays the remaining distance to the destination.
   - **Properties**:
     - `fuel_rate` and `velocity` are validated to stay within their respective ranges.

### 3. **Employee Class (Inherits from Person)**
   - Represents an employee with additional attributes:
     - `id`: Employee ID.
     - `email`: Employee email.
     - `salary`: Employee salary.
     - `distance_to_work`: Distance to the workplace.
     - `car`: Optional car object associated with the employee.
   - **Methods**:
     - `work(hours)`: Updates the mood based on hours worked.
     - `drive(distance, velocity)`: Drives the car for a given distance and velocity.
     - `refuel(gas_amount)`: Refuels the car.
     - `send_mail(recipient, subject, body)`: Simulates sending an email.

### 4. **Office Class**
   - Represents an office with attributes:
     - `name`: Name of the office.
     - `employees`: List of employees in the office.
   - **Methods**:
     - `get_all_employees()`: Returns a list of all employees.
     - `get_employee(emp_id)`: Returns the employee with the given ID.
     - `hire(employee)`: Hires an employee.
     - `fire(emp_id)`: Fires an employee.
     - `deduct(emp_id, deduction)`: Deducts money from an employee's salary.
     - `reward(emp_id, reward)`: Rewards an employee with additional salary.
     - `check_lateness(emp_id, move_hour)`: Checks if an employee is late and deducts or rewards accordingly.
   - **Static Method**:
     - `calculate_lateness(target_hour, move_hour, distance, velocity)`: Calculates if an employee is late based on their move hour, distance, and velocity.

