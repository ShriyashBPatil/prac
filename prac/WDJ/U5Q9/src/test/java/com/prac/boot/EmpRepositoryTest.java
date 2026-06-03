package com.prac.boot;
import com.prac.boot.entity.Emp;
import com.prac.boot.repository.EmpRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
public class EmpRepositoryTest {
    @Autowired
    private EmpRepository repo;
    
    @Test
    public void testSaveEmp() {
        Emp e = new Emp();
        e.setEid(101);
        e.setEname("Test User");
        e.setDept("IT");
        e.setSal(50000);
        
        Emp saved = repo.save(e);
        assertThat(saved.getEid()).isEqualTo(101);
    }
}
