package com.prac.boot.service;
import com.prac.boot.entity.Emp;
import com.prac.boot.repository.EmpRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class EmpService {
    @Autowired
    private EmpRepository repo;
    
    public List<Emp> getAll() { return repo.findAll(); }
    public Emp save(Emp e) { return repo.save(e); }
    public void delete(int id) { repo.deleteById(id); }
}
