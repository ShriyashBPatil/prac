package com.prac.boot.service;
import com.prac.boot.model.Product;
import com.prac.boot.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository repo;
    
    public List<Product> getAll() { return repo.findAll(); }
    public void addProduct(Product p) { repo.save(p); }
    public void updateProduct(int id, Product p) {
        Product existing = repo.findById(id);
        if(existing != null) { existing.setName(p.getName()); }
    }
    public void deleteProduct(int id) { repo.delete(id); }
}
