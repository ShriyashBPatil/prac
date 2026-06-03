package annotationdi;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import annotationdi.Student;
import annotationdi.StudentService;

@RestController
@RequestMapping("/students")
public class StudentController {

    @Autowired
    private StudentService service;

    @GetMapping
    public List<Student> getStudents() {
        return service.getStudents();
    }

    @PostMapping
    public String addStudent(@RequestBody Student student) {
        service.addStudent(student);
        return "Student Added";
    }

    @PutMapping("/{id}")
    public String updateStudent(@PathVariable int id,
                                @RequestBody Student student) {
        service.updateStudent(id, student);
        return "Student Updated";
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable int id) {
        service.deleteStudent(id);
        return "Student Deleted";
    }
}