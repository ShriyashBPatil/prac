package com.mca;


import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class U5Q2Application {

    public static void main(String[] args) {

        ApplicationContext context =
                new ClassPathXmlApplicationContext("applicationContext.xml");

        // Constructor Injection
        College c = (College) context.getBean("college");
        c.show();

        // Setter Injection
        School s = (School) context.getBean("school");
        s.show();
    }
}