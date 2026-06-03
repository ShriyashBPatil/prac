package annotationdi;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class Student {

    @Value("101")
    private int id;

    @Value("STD")
    private String name;

    public void display() {
        System.out.println("Student ID : " + id);
        System.out.println("Student Name : " + name);
    }
}