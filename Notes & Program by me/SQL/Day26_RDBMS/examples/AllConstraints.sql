CREATE TABLE EmployeeProfiles (
    EmpID INT PRIMARY KEY,
    AadharNumber VARCHAR(12) UNIQUE,
    Age INT CHECK (Age >= 18),
    City VARCHAR(50) DEFAULT 'New York',
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);