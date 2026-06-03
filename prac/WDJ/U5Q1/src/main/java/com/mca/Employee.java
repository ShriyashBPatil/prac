package com.mca;

public class Employee {

    private int id;
    private String name;

    public void setId(int id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void display() {
        System.out.println("ID : " + id);
        System.out.println("Name : " + name);
    }
}