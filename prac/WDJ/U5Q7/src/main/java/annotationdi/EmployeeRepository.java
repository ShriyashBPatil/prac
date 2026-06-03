package annotationdi;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import annotationdi.Employee;

@Repository
public interface EmployeeRepository
       extends JpaRepository<Employee,Integer> {

}