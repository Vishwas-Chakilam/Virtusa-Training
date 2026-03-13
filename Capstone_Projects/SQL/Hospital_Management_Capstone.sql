-- -----------------------------------------------------------------------------
-- CAPSTONE DATABAE MODEL: Comprehensive Hospital Management System
-- -----------------------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS HospitalMgmtDB;
USE HospitalMgmtDB;

-- 1. Departments Hierarchy
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY AUTO_INCREMENT,
    DeptName VARCHAR(100) UNIQUE NOT NULL,
    Location VARCHAR(100)
);

-- 2. Staffing and Doctors
CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(150) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID) ON DELETE SET NULL
);

-- 3. Patient Registry
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(150) NOT NULL,
    DOB DATE NOT NULL,
    Gender ENUM('M', 'F', 'O'),
    ContactNumber VARCHAR(20) UNIQUE
);

-- 4. Admissions Logistics
CREATE TABLE Admissions (
    AdmissionID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT,
    DoctorID INT,
    AdmissionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    DischargeDate DATETIME,
    Diagnosis TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- 5. Billing System
CREATE TABLE Billings (
    BillID INT PRIMARY KEY AUTO_INCREMENT,
    AdmissionID INT,
    TotalAmount DECIMAL(12, 2) NOT NULL,
    PaymentStatus ENUM('PENDING', 'PARTIAL', 'COMPLETED') DEFAULT 'PENDING',
    FOREIGN KEY (AdmissionID) REFERENCES Admissions(AdmissionID)
);

-- PROCEDURES & VIEWS --
DELIMITER //
CREATE PROCEDURE DischargePatient(IN p_AdmissionID INT)
BEGIN
    UPDATE Admissions 
    SET DischargeDate = CURRENT_TIMESTAMP 
    WHERE AdmissionID = p_AdmissionID;
END //
DELIMITER ;

CREATE VIEW ActivePatients AS
SELECT p.FullName AS PatientName, d.FullName AS DoctorName, a.AdmissionDate
FROM Admissions a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID
WHERE a.DischargeDate IS NULL;