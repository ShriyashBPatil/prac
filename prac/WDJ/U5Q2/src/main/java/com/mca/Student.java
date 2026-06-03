package com.mca;


public class Student {

    private String name;

    // Setter Method
    public void setName(String name) {
        this.name = name;
    }

    public void display() {
        System.out.println("Student Name: " + name);
    }
}