-- Create Table
CREATE TABLE Users (
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alter Table to add column
ALTER TABLE Users ADD LastLogin DATE;

-- Drop (Commented out to prevent accidental drop)
-- DROP TABLE Users;
