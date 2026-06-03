package com.mca;


public class College {

    private Student student;

    // Constructor Injection
    public College(Student student) {
        this.student = student;
    }

    public void show() {
        student.display();
    }
}