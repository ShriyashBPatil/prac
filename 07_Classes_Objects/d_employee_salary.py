# Program 7d: Employee class to calculate total salary (Basic + HRA + DA)

class Employee:
    def __init__(self, name, emp_id, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary

    def calculate_hra(self):
        """HRA = 20% of Basic Salary"""
        return self.basic_salary * 0.20

    def calculate_da(self):
        """DA = 30% of Basic Salary"""
        return self.basic_salary * 0.30

    def total_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Basic Salary: ₹{self.basic_salary}")
        print(f"HRA (20%): ₹{self.calculate_hra()}")
        print(f"DA (30%): ₹{self.calculate_da()}")
        print(f"Total Salary: ₹{self.total_salary()}")


# Creating object
emp = Employee("Shriyash", "EMP001", 30000)
print("Employee Details:")
emp.display()
