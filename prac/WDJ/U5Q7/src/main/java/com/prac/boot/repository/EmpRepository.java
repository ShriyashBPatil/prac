package com.prac.boot.repository;
import com.prac.boot.entity.Emp;
import org.springframework.data.jpa.repository.JpaRepository;
public interface EmpRepository extends JpaRepository<Emp, Integer> {
}
