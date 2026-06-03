package com.prac.boot.controller;
import com.prac.boot.exception.ResourceNotFoundException;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @GetMapping("/user/{id}")
    public String getUser(@PathVariable int id) {
        if(id > 100) {
            throw new ResourceNotFoundException("User not found with ID: " + id);
        }
        return "User details for " + id;
    }
}
