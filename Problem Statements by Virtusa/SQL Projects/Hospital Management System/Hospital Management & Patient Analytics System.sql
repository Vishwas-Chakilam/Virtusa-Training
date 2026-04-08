-- hospital management system script
-- created to manage doctors, patients and bills

-- setting up the database
create database if not exists hospital_db;
use hospital_db;

-- table for patients
create table patients (
    pid int primary key auto_increment,
    name varchar(150) not null,
    age int,
    sex varchar(15)
);

-- table for doctors
create table doctors (
    did int primary key auto_increment,
    name varchar(150) not null,
    spec varchar(100) not null
);

-- table for appointments
create table appointments (
    aid int primary key auto_increment,
    pid int,
    did int,
    a_date date,
    foreign key (pid) references patients(pid),
    foreign key (did) references doctors(did)
);

-- table for medical bills / treatments
create table bills (
    bid int primary key auto_increment,
    pid int,
    issue varchar(255) not null,
    cost decimal(10, 2) not null, 
    b_date date,
    foreign key (pid) references patients(pid)
);

-- adding some test data
insert into patients (name, age, sex) values 
('suresh kumar', 45, 'male'),
('meena kumari', 32, 'female'),
('rajesh patel', 29, 'male'),
('sunita sharma', 50, 'female'),
('amit singh', 24, 'male');

insert into doctors (name, spec) values 
('dr. gupta', 'cardiology'),
('dr. sharma', 'general medicine'),
('dr. rao', 'dermatology'),
('dr. mehta', 'pediatrics');

insert into appointments (pid, did, a_date) values 
(1, 1, '2024-02-10'),
(2, 2, '2024-02-11'),
(1, 2, '2024-02-12'),
(3, 3, '2024-03-01'),
(4, 4, '2024-03-05'),
(5, 1, '2024-03-10'),
(2, 4, '2024-04-02');

insert into bills (pid, issue, cost, b_date) values 
(1, 'hypertension', 5000.00, '2024-02-10'),
(2, 'common cold', 500.00, '2024-02-11'),
(3, 'skin rash', 1200.00, '2024-03-01'),
(4, 'seasonal fever', 800.00, '2024-03-05'),
(5, 'high blood pressure', 1500.00, '2024-03-10'),
(1, 'routine followup', 1000.00, '2024-04-15');

-- 1. seeing which doctors are busiest
select d.name, count(a.aid) as total
from doctors d
join appointments a on d.did = a.did
group by d.name
order by total desc;

-- 2. total money made per month
select monthname(b_date) as month, sum(cost) as revenue
from bills
group by month
order by revenue desc;

-- 3. common diseases/issues
select issue, count(*) as count
from bills
group by issue
order by count desc;

-- 4. patient visit frequency
select p.name, count(a.aid) as visits
from patients p
join appointments a on p.pid = a.pid
group by p.name
order by visits desc;

-- 5. how many unique patients each doctor saw
select d.name, count(distinct a.pid) as patients
from doctors d
join appointments a on d.did = a.did
group by d.name
order by patients desc;