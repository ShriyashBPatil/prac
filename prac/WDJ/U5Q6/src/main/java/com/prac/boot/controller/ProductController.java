package com.prac.boot.controller;
import com.prac.boot.model.Product;
import com.prac.boot.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {
    @Autowired
    private ProductService service;
    
    @GetMapping
    public List<Product> getAll() { return service.getAll(); }
    
    @PostMapping
    public String add(@RequestBody Product p) { service.addProduct(p); return "Added!"; }
    
    @PutMapping("/{id}")
    public String update(@PathVariable int id, @RequestBody Product p) { service.updateProduct(id, p); return "Updated!"; }
    
    @DeleteMapping("/{id}")
    public String delete(@PathVariable int id) { service.deleteProduct(id); return "Deleted!"; }
}
