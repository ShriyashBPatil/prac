# Program 8g: Encapsulation: Employee with private salary (Getter/Setter)

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.__salary = salary  # Private variable

    # Getter
    @property
    def salary(self):
        return self.__salary

    # Setter
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Salary updated to ₹{new_salary}")
        else:
            print("Salary must be positive!")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ₹{self.__salary}")


# Creating object
emp = Employee("Shriyash", "EMP001", 50000)
print("Encapsulation with Getter/Setter:")
print("-" * 40)
emp.display()

# Using setter
print()
emp.salary = 60000
emp.display()

# Using getter
print(f"\nUsing getter: ₹{emp.salary}")
