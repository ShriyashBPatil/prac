package annotationdi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class School {

    private Student student;

    @Autowired
    public void setStudent(Student student) {
        this.student = student;
    }

    public void show() {
        System.out.println("\nSetter Injection");
        student.display();
    }
}