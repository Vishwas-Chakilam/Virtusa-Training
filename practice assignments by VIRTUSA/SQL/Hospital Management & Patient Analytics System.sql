-- My SQL Capstone Project: Hospital Management System
-- I made this to track patients, doctors, and all the treatment data.

-- First, I'm setting up the database
CREATE DATABASE IF NOT EXISTS HospitalManagementDB;
USE HospitalManagementDB;

-- Table for patient info
-- I used p_name for full name and added age / gender
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(150) NOT NULL,
    age INT,
    gender VARCHAR(15)
);

-- Table for doctor details
-- This stores their name and what they specialize in
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    d_name VARCHAR(150) NOT NULL,
    specialization VARCHAR(100) NOT NULL
);

-- Table for booking appointments
-- This connects the patient to the doctor on a certain date
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

-- Table for treatments and costs
-- diagnosis is the disease and fees is the cost of treatment
CREATE TABLE Treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    diagnosis VARCHAR(255) NOT NULL,
    fees DECIMAL(10, 2) NOT NULL, 
    treatment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Now adding some sample records to test the project
INSERT INTO Patients (p_name, age, gender) VALUES 
('Suresh Kumar', 45, 'Male'),
('Meena Kumari', 32, 'Female'),
('Rajesh Patel', 29, 'Male'),
('Sunita Sharma', 50, 'Female'),
('Amit Singh', 24, 'Male');

INSERT INTO Doctors (d_name, specialization) VALUES 
('Dr. Gupta', 'Cardiology'),
('Dr. Sharma', 'General Medicine'),
('Dr. Rao', 'Dermatology'),
('Dr. Mehta', 'Pediatrics');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date) VALUES 
(1, 1, '2024-02-10'),
(2, 2, '2024-02-11'),
(1, 2, '2024-02-12'),
(3, 3, '2024-03-01'),
(4, 4, '2024-03-05'),
(5, 1, '2024-03-10'),
(2, 4, '2024-04-02');

INSERT INTO Treatments (patient_id, diagnosis, fees, treatment_date) VALUES 
(1, 'Hypertension', 5000.00, '2024-02-10'),
(2, 'Common Cold', 500.00, '2024-02-11'),
(3, 'Skin Rash', 1200.00, '2024-03-01'),
(4, 'Seasonal Fever', 800.00, '2024-03-05'),
(5, 'High Blood Pressure', 1500.00, '2024-03-10'),
(1, 'Routine Followup', 1000.00, '2024-04-15');


-- Queries for the project tasks

-- 1. Find the busiest / most consulted doctors
-- I'm counting appointments grouped by doctor name
SELECT d.d_name, COUNT(a.appointment_id) AS total_consultations
FROM Doctors d
JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.d_name
ORDER BY total_consultations DESC;

-- 2. Figure out the total revenue for each month
-- Using monthname to make it look nicer
SELECT MONTHNAME(treatment_date) AS month_name, SUM(fees) AS monthly_revenue
FROM Treatments
GROUP BY month_name
ORDER BY monthly_revenue DESC;

-- 3. What are the most common diseases found?
SELECT diagnosis, COUNT(*) AS disease_count
FROM Treatments
GROUP BY diagnosis
ORDER BY disease_count DESC;

-- 4. Tracking how often patients visit
SELECT p.p_name, COUNT(a.appointment_id) AS visit_count
FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
GROUP BY p.p_name
ORDER BY visit_count DESC;

-- 5. Doctor performance (how many unique patients they handle)
SELECT d.d_name, COUNT(DISTINCT a.patient_id) AS unique_patients
FROM Doctors d
JOIN Appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.d_name
ORDER BY unique_patients DESC;


-- Just some testing queries to check the data
SELECT * FROM Patients WHERE age > 30;
SELECT * FROM Treatments WHERE fees < 1000.00;