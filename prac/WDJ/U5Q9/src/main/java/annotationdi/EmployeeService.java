package annotationdi;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import annotationdi.Employee;
import annotationdi.EmployeeRepository;

@Service
public class EmployeeService {

    @Autowired
    private EmployeeRepository repo;

    public List<Employee> getAllEmployees() {
        return repo.findAll();
    }

    public Employee addEmployee(Employee emp) {
        return repo.save(emp);
    }

    public Employee updateEmployee(Employee emp) {
        return repo.save(emp);
    }

    public void deleteEmployee(int id) {
        repo.deleteById(id);
    }
}