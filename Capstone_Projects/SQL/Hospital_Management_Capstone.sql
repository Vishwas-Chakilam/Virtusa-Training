-- sql capston project for hospital managment 
-- this is my final work

-- first makeing the database
CREATE DATABASE hospital_new;
USE hospital_new;

-- Table for patient data
-- i think p_name is okay
CREATE TABLE Patients (
    pat_id INT PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(255),
    age INT,
    gender VARCHAR(50)
);

-- table for doctors
-- i added specalization here for doctor type
CREATE TABLE Doctors (
    doc_id INT PRIMARY KEY AUTO_INCREMENT,
    d_name VARCHAR(255),
    specalization VARCHAR(255)
);

-- Table for booking apointments
-- this will link paitient and doctor together
CREATE TABLE Appointments (
    app_id INT PRIMARY KEY AUTO_INCREMENT,
    p_id INT,
    d_id INT,
    app_date DATE
);

-- Table for treatement and costs
-- diagnosis is basically the diease name
CREATE TABLE Treatments (
    treat_id INT PRIMARY KEY AUTO_INCREMENT,
    pat_id INT,
    diease VARCHAR(255),
    fees INT, 
    t_date DATE
);

-- inserting some test data
-- using unique name for patiants
INSERT INTO Patients (p_name, age, gender) VALUES ('Suresh Kumar', 45, 'Male');
INSERT INTO Patients (p_name, age, gender) VALUES ('Meena Kumari', 32, 'Female');
INSERT INTO Patients (p_name, age, gender) VALUES ('Rajesh Patel', 29, 'Male');
INSERT INTO Patients (p_name, age, gender) VALUES ('Sunita Sharma', 50, 'Female');
INSERT INTO Patients (p_name, age, gender) VALUES ('Amit Singh', 24, 'Male');

-- adding doctors info
INSERT INTO Doctors (d_name, specalization) VALUES ('Dr. Gupta', 'Cardio');
INSERT INTO Doctors (d_name, specalization) VALUES ('Dr. Sharma', 'General');
INSERT INTO Doctors (d_name, specalization) VALUES ('Dr. Rao', 'Skin');
INSERT INTO Doctors (d_name, specalization) VALUES ('Dr. Mehta', 'Child');

-- apointment dates
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (1, 1, '2024-02-10');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (2, 2, '2024-02-11');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (1, 2, '2024-02-12');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (3, 3, '2024-03-01');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (4, 4, '2024-03-05');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (5, 1, '2024-03-10');
INSERT INTO Appointments (p_id, d_id, app_date) VALUES (2, 4, '2024-04-02');

-- treatment and diease data
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (1, 'Heart Pain', 5000, '2024-02-10');
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (2, 'Cold', 500, '2024-02-11');
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (3, 'Rash', 1200, '2024-03-01');
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (4, 'Fever', 800, '2024-03-05');
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (5, 'High BP', 1500, '2024-03-10');
INSERT INTO Treatments (pat_id, diease, fees, t_date) VALUES (1, 'Followup', 1000, '2024-04-15');

-- TASK 1: Find most consulted doctors
-- i will count how many times each doctor id is in appointments
SELECT d_name, count(*) as total
FROM Doctors, Appointments
WHERE Doctors.doc_id = Appointments.d_id
GROUP BY d_name
ORDER BY total DESC;

-- TASK 2: total revenue per month
-- used month function here
SELECT month(t_date) as t_month, sum(fees) as total_money
FROM Treatments
GROUP BY t_month;

-- TASK 3: Identify most common dieases
-- count grouped by diease
SELECT diease, count(*) as frequency
FROM Treatments
GROUP BY diease
ORDER BY frequency DESC;

-- TASK 4: Track patient visit frequency
-- count how many times patient came
SELECT p_name, count(*) as visits
FROM Patients, Appointments
WHERE Patients.pat_id = Appointments.p_id
GROUP BY p_name
ORDER BY visits DESC;

-- TASK 5: Analyze doctor performance
-- using count for now
SELECT d_name, count(*) from Doctors d, Appointments a 
where d.doc_id = a.d_id 
group by d_name;

-- tests
select * from Patients where age > 30;
select * from Treatments where fees < 1000;