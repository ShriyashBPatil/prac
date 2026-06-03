package com.prac.boot.repository;
import com.prac.boot.model.Product;
import org.springframework.stereotype.Repository;
import java.util.ArrayList;
import java.util.List;

@Repository
public class ProductRepository {
    private List<Product> products = new ArrayList<>();
    
    public List<Product> findAll() { return products; }
    public void save(Product p) { products.add(p); }
    public Product findById(int id) {
        return products.stream().filter(p -> p.getId() == id).findFirst().orElse(null);
    }
    public void delete(int id) { products.removeIf(p -> p.getId() == id); }
}
