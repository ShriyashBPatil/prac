package com.shriyash.mca.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.shriyash.mca.model.Student;

@RestController
@RequestMapping("/students")
public class StudentController {
    private List<Student> students = new ArrayList<>();

    public StudentController() {
        students.add(new Student(1, "Shriyash"));
    }

    @GetMapping
    public List<Student> getAllStudents() {
        return students;
    }

    @GetMapping("/{id}")
    public Student getStudentById(@PathVariable int id) {
        for (Student s : students) {
            if (s.getId() == id) {
                return s;
            }
        }
        return null;
    }

    @PostMapping
    public String addStudent(@RequestBody Student student) {
        students.add(student);
        return "Student added successfully";
    }

    @PutMapping("/{id}")
    public String updateStudent(@PathVariable int id, @RequestBody Student student) {
        for (Student s : students) {
            if (s.getId() == id) {
                s.setName(student.getName());
                return "Student updated successfully";
            }
        }
        return "Student not found";
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable int id) {
        students.removeIf(s -> s.getId() == id);
        return "Student deleted successfully";
    }
}
