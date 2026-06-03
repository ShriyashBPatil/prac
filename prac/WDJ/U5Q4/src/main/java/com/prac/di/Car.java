package com.prac.di;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Car {
    private Engine engine;
    private String model;

    // Constructor Injection
    @Autowired
    public Car(Engine engine) {
        this.engine = engine;
    }

    // Setter Injection
    @Autowired
    public void setModel(String model) {
        this.model = model; // In a real app this might come from properties
    }

    public void drive() {
        engine.start();
        System.out.println("Driving car model: " + (model != null ? model : "DefaultModel"));
    }
}
