package com.prac.di;
public class Vehicle {
    private String brand;
    // Setter
    public void setBrand(String brand) {
        this.brand = brand;
    }
    public void show() {
        System.out.println("Vehicle brand is: " + brand);
    }
}
