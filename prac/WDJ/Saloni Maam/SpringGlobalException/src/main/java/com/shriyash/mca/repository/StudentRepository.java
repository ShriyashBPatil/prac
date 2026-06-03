package com.shriyash.mca.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.shriyash.mca.model.Student;

@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
}
