CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2),
    Category VARCHAR(50)
);

INSERT INTO Products (ProductName, Price, Category) VALUES 
('Laptop', 1200.00, 'Electronics'),
('Chair', 50.00, 'Furniture'),
('Desk', 150.00, 'Furniture'),
('Phone', 800.00, 'Electronics');

UPDATE Products SET Price = Price * 1.1 WHERE Category = 'Electronics';
