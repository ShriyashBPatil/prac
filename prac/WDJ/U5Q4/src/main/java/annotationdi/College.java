package annotationdi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class College {

    private Student student;

    @Autowired
    public College(Student student) {
        this.student = student;
    }

    public void show() {
        System.out.println("\nConstructor Injection");
        student.display();
    }
}