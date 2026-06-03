package di;

public class Employee {

    private String name;

    public void setName(String name) {
        this.name = name;
    }

    public void display() {
        System.out.println("Employee Name: " + name);
    }
}