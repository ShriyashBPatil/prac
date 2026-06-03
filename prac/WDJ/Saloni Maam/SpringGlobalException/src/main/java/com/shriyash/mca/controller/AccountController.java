package com.shriyash.mca.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.shriyash.mca.model.Account;
import com.shriyash.mca.service.AccountService;

@RestController
@RequestMapping("/api/accounts")
public class AccountController {

    @Autowired
    private AccountService accountService;

    @PostMapping
    public ResponseEntity<Account> createAccount(@RequestBody Account account) {
        return ResponseEntity.ok(accountService.createAccount(account));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Account> getAccount(@PathVariable Long id) {
        return ResponseEntity.ok(accountService.getAccount(id));
    }

    @PostMapping("/transfer")
    public ResponseEntity<String> transferMoney(
            @RequestParam Long fromAccountId,
            @RequestParam Long toAccountId,
            @RequestParam Double amount,
            @RequestParam(defaultValue = "false") boolean simulateError) {
        
        accountService.transferMoney(fromAccountId, toAccountId, amount, simulateError);
        return ResponseEntity.ok("Transfer successful");
    }
}
