package annotationdi;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import annotationdi.Employee;
import annotationdi.EmployeeService;

@RestController
@RequestMapping("/employee")
public class EmployeeController {

    @Autowired
    private EmployeeService service;

    @GetMapping
    public List<Employee> getEmployees() {
        return service.getAllEmployees();
    }

    @PostMapping
    public Employee addEmployee(
            @RequestBody Employee emp) {

        return service.addEmployee(emp);
    }

    @PutMapping
    public Employee updateEmployee(
            @RequestBody Employee emp) {

        return service.updateEmployee(emp);
    }

    @DeleteMapping("/{id}")
    public String deleteEmployee(
            @PathVariable int id) {

        service.deleteEmployee(id);

        return "Employee Deleted";
    }
}