package di;

public class Company {

    private Employee employee;

    // Setter Injection
    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

    public void show() {
        employee.display();
    }
}