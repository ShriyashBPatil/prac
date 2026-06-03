package com.shriyash.mca.controller;

import org.springframework.web.bind.annotation.*;
import com.shriyash.mca.model.Book;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {
    private List<Book> books = new ArrayList<>();

    public BookController() {
        books.add(new Book(1, "The Great Gatsby", "F. Scott Fitzgerald"));
    }

    @GetMapping
    public List<Book> getAllBooks() {
        return books;
    }

    @GetMapping("/{id}")
    public Book getBookById(@PathVariable int id) {
        for (Book b : books) {
            if (b.getBookId() == id) {
                return b;
            }
        }
        return null;
    }

    @PostMapping
    public String addBook(@RequestBody Book book) {
        books.add(book);
        return "Book added successfully";
    }

    @PutMapping("/{id}")
    public String updateBook(@PathVariable int id, @RequestBody Book book) {
        for (Book b : books) {
            if (b.getBookId() == id) {
                b.setTitle(book.getTitle());
                b.setAuthor(book.getAuthor());
                return "Book updated successfully";
            }
        }
        return "Book not found";
    }

    @DeleteMapping("/{id}")
    public String deleteBook(@PathVariable int id) {
        books.removeIf(b -> b.getBookId() == id);
        return "Book deleted successfully";
    }
}
