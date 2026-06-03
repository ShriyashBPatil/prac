package com.prac.boot;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.CommandLineRunner;

@SpringBootApplication
public class U5Q5Application implements CommandLineRunner {
    public static void main(String[] args) {
        SpringApplication.run(U5Q5Application.class, args);
    }
    
    @Override
    public void run(String... args) {
        System.out.println("===============================");
        System.out.println("My First Spring Application");
        System.out.println("===============================");
    }
}
