package annotationdi;


import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import annotationdi.Student;

@Repository
public class StudentRepository {

    private List<Student> students = new ArrayList<>();

    public List<Student> getAllStudents() {
        return students;
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void updateStudent(int id, Student student) {
        for(Student s : students) {
            if(s.getId() == id) {
                s.setName(student.getName());
            }
        }
    }

    public void deleteStudent(int id) {
        students.removeIf(s -> s.getId() == id);
    }
}