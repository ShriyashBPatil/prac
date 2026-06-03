package com.example.payment;

public class PaymentProcessor {

    private PaymentService paymentService;

    public void setPaymentService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void processPayment(double amount) {
        paymentService.pay(amount);
    }
}
