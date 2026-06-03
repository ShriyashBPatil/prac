package com.example.notification;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
        NotificationManager manager = (NotificationManager) context.getBean("notificationManager");
        manager.notifyUser("Order Successfully!");
    }
}
