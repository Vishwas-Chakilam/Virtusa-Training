import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String msg) { super(msg); }
}

class Account {
    private String accountNumber;
    private double balance;
    private List<String> transactionHistory;

    public Account(String accNo, double initBalance) {
        this.accountNumber = accNo;
        this.balance = initBalance;
        this.transactionHistory = new ArrayList<>();
        transactionHistory.add("Account created with balance: $" + initBalance);
    }

    public String getAccountNumber() { return accountNumber; }
    public double getBalance() { return balance; }

    public synchronized void deposit(double amount) {
        if(amount > 0) {
            balance += amount;
            transactionHistory.add("Deposited: $" + amount + " | New Balance: $" + balance);
        }
    }

    // TODO: handling concurrent withdrawals needs better testing.\n    public synchronized void withdraw(double amount) throws InsufficientFundsException {
        if(amount > balance) {
            throw new InsufficientFundsException("Cannot withdraw $" + amount + ". Current balance: $" + balance);
        }
        balance -= amount;
        transactionHistory.add("Withdrawn: $" + amount + " | New Balance: $" + balance);
    }
    
    public void printStatement() {
        System.out.println("Statement for " + accountNumber + ":");
        transactionHistory.forEach(System.out::println);
    }
}

public class BankingSystemCapstone {
    // using concurrent hashmap for thread safety b/c basic hashmap was crashing on multi threads
    private Map<String, Account> accountsDB = new ConcurrentHashMap<>();

    public void registerAccount(String accNo, double initBalance) {
        accountsDB.put(accNo, new Account(accNo, initBalance));
        System.out.println("Account " + accNo + " generated.");
    }
    
    public void performTransfer(String fromId, String toId, double amount) {
        Account from = accountsDB.get(fromId);
        Account to = accountsDB.get(toId);
        
        if(from != null && to != null) {
            try {
                from.withdraw(amount);
                to.deposit(amount);
                System.out.println("Successfully transferred $" + amount + " from " + fromId + " to " + toId);
            } catch (InsufficientFundsException e) {
                System.err.println("Transfer Failed: " + e.getMessage());
            }
        } else {
            System.err.println("Transfer Failed: Invalid account number(s).");
        }
    }

    public static void main(String[] args) {
        System.out.println("--- Core Banking System Capstone ---");
        BankingSystemCapstone bank = new BankingSystemCapstone();
        
        bank.registerAccount("ACC100", 500.0);
        bank.registerAccount("ACC200", 150.0);
        
        bank.performTransfer("ACC100", "ACC200", 200.0);
        bank.performTransfer("ACC200", "ACC100", 400.0); // Should fail
        
        System.out.println("\nFinal Statements:");
        bank.accountsDB.get("ACC100").printStatement();
        bank.accountsDB.get("ACC200").printStatement();
    }
}