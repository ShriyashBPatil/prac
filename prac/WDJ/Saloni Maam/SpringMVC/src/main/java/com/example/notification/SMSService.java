package com.example.notification;

public class SMSService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        System.out.println("SMS Sent: " + message);
    }
}
