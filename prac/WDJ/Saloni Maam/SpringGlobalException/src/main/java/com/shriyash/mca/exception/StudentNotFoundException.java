package com.shriyash.mca.exception;

public class StudentNotFoundException extends RuntimeException {
    
    public StudentNotFoundException(Long id) {
        super("Student record with ID " + id + " not found.");
    }
}
