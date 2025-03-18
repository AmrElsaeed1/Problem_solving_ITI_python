# Multilevel Inheritance Example

This project demonstrates **multilevel inheritance** in Python using the `super()` function. It includes three classes: `Person`, `Employee`, and `Manager`. Each class builds upon the previous one, adding new attributes and methods while reusing the functionality of the parent class.

---

## Class Hierarchy

1. **`Person` (Base Class)**:
   - Represents a generic person with attributes `name` and `age`.
   - Contains a method `display_info()` to display the person's name and age.

2. **`Employee` (Derived from `Person`)**:
   - Represents an employee with additional attributes `employee_id` and `salary`.
   - Overrides the `display_info()` method to include employee-specific details.

3. **`Manager` (Derived from `Employee`)**:
   - Represents a manager with an additional attribute `department`.
   - Overrides the `display_info()` method to include manager-specific details.

---

## Key Features

1. **Multilevel Inheritance**:
   - `Employee` inherits from `Person`.
   - `Manager` inherits from `Employee`.

2. **Use of `super()`**:
   - `super()` is used to call the parent class's `__init__` method, ensuring that attributes from the parent class are properly initialized.
   - `super()` is also used to call the parent class's `display_info()` method, allowing each class to add its own information while reusing the parent class's functionality.

3. **Method Overriding**:
   - Each class overrides the `display_info()` method to add its own specific details while still calling the parent class's `display_info()` method.

---
