package com.example.payment;

public class CreditCardPayment implements PaymentService {
    public void pay(double amount) {
        System.out.println("Paid " + amount + " using Credit Card");
    }
}
