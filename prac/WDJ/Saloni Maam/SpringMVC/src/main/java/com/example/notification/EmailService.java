package com.example.notification;

public class EmailService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        System.out.println("Email Sent: " + message);
    }
}
