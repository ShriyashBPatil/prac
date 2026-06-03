package com.mca;

public class School {

    private Student student;

    // Setter Injection
    public void setStudent(Student student) {
        this.student = student;
    }

    public void show() {
        student.display();
    }
}