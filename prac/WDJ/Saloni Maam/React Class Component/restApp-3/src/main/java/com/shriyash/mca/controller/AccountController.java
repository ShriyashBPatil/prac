package com.shriyash.mca.controller;

import com.shriyash.mca.entity.Account;
import com.shriyash.mca.repository.AccountRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/bank")
@CrossOrigin(origins = "http://localhost:3000")
public class AccountController {

    @Autowired
    private AccountRepository accountRepository;

    @GetMapping("/show")
    public List<Account> getAllAccounts() {
        return accountRepository.findAll();
    }

    @PostMapping("/create")
    public Account createAccount(@RequestBody Account account) {
        return accountRepository.save(account);
    }
}
