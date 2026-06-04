# Program 8d: Method Overriding: Employee work() in Manager/Developer

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")


class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team and conducting meetings.")


class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code and debugging software.")


# Creating objects
print("Method Overriding Example:")
print("-" * 50)

emp = Employee("Generic Employee")
emp.work()

mgr = Manager("Rahul")
mgr.work()

dev = Developer("Shriyash")
dev.work()
