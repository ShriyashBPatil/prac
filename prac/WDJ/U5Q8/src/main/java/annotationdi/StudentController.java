package annotationdi;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.*;

import annotationdi.StudentNotFoundException;
import annotationdi.Student;

@RestController
@RequestMapping("/student")
public class StudentController {

    List<Student> students = new ArrayList<>();

    public StudentController() {

        students.add(new Student(1, "Shriyash"));
        students.add(new Student(2, "Rahul"));
        students.add(new Student(3, "Saloni"));
    }

    @GetMapping("/{id}")
    public Student getStudent(@PathVariable int id) {

        return students.stream()
                .filter(s -> s.getId() == id)
                .findFirst()
                .orElseThrow(() ->
                    new StudentNotFoundException(
                        "Student ID " + id + " Not Found"));
    }
}