CREATE DATABASE IF NOT EXISTS BankingDB;
USE BankingDB;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(100) NOT NULL,
    KYCStatus BOOLEAN DEFAULT FALSE
);

CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    Balance DECIMAL(15,2) DEFAULT 0.00,
    Status ENUM('ACTIVE', 'DORMANT', 'CLOSED') DEFAULT 'ACTIVE',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Transactions (
    TxID INT PRIMARY KEY AUTO_INCREMENT,
    AccountID INT,
    TxType ENUM('DEPOSIT', 'WITHDRAWAL', 'TRANSFER'),
    Amount DECIMAL(15,2) NOT NULL CHECK(Amount > 0),
    TxDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

-- Index to query large volume of transactions quickly based on account
CREATE INDEX idx_trans_acc ON Transactions(AccountID);