CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10,2),
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);

INSERT INTO Departments VALUES (1, 'HR'), (2, 'IT'), (3, 'Finance');
INSERT INTO Employees VALUES (101, 'Alice', 1, 50000), (102, 'Bob', 2, 70000), (103, 'Charlie', 2, 80000), (104, 'David', NULL, 40000);
