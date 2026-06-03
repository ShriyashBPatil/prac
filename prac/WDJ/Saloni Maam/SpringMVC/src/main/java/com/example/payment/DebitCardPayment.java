package com.example.payment;

public class DebitCardPayment implements PaymentService {
    public void pay(double amount) {
        System.out.println("Paid " + amount + " using Debit Card");
    }
}
