package annotationdi;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import annotationdi.Student;
import annotationdi.StudentRepository;

@Service
public class StudentService {

    @Autowired
    private StudentRepository repository;

    public List<Student> getStudents() {
        return repository.getAllStudents();
    }

    public void addStudent(Student student) {
        repository.addStudent(student);
    }

    public void updateStudent(int id, Student student) {
        repository.updateStudent(id, student);
    }

    public void deleteStudent(int id) {
        repository.deleteStudent(id);
    }
}