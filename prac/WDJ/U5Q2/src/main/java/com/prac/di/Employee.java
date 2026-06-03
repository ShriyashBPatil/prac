package com.prac.di;
public class Employee {
    private int id;
    private String name;
    
    // Constructor Injection
    public Employee(int id) {
        this.id = id;
    }
    
    // Setter Injection
    public void setName(String name) {
        this.name = name;
    }
    
    public void show() {
        System.out.println("Employee ID: " + id + ", Name: " + name);
    }
}
