package com.prac.boot.controller;
import com.prac.boot.entity.Emp;
import com.prac.boot.service.EmpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/emps")
public class EmpController {
    @Autowired
    private EmpService service;
    
    @GetMapping
    public List<Emp> getAll() { return service.getAll(); }
    
    @PostMapping
    public Emp add(@RequestBody Emp e) { return service.save(e); }
    
    @PutMapping("/{id}")
    public Emp update(@PathVariable int id, @RequestBody Emp e) { e.setEid(id); return service.save(e); }
    
    @DeleteMapping("/{id}")
    public String delete(@PathVariable int id) { service.delete(id); return "Deleted!"; }
}
