# Program 3g: Display student details using **kwargs

def display_student(**kwargs):
    """Display student details using **kwargs."""
    print("Student Details:")
    print("-" * 30)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
    print()


display_student(name="Shriyash", roll_no=101, branch="Computer Science", marks=85)

display_student(name="Rahul", roll_no=102, branch="IT", marks=90, city="Pune")
