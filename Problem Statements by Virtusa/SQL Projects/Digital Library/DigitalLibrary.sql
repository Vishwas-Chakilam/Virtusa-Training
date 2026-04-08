-- library database audit script
-- for community college books tracking

-- setting up the tables
create table books (
    book_id int primary key,
    title varchar(255) not null,
    author varchar(255),
    category varchar(100),
    isbn varchar(20) unique
);

create table students (
    student_id int primary key,
    fname varchar(100) not null,
    lname varchar(100) not null,
    email varchar(255) unique,
    join_date date default current_date
);

create table issues (
    issue_id int primary key auto_increment,
    book_id int,
    student_id int,
    issue_date date not null,
    return_date date,
    foreign key (book_id) references books(book_id),
    foreign key (student_id) references students(student_id)
);

-- adding some dummy data to test
insert into books (book_id, title, author, category, isbn) values
(101, 'python for beginners', 'guido van rossum', 'science', 'isbn101'),
(102, 'the great gatsby', 'f. scott fitzgerald', 'fiction', 'isbn102'),
(103, 'a short history of nearly everything', 'bill bryson', 'history', 'isbn103'),
(104, 'introduction to algorithms', 'thomas cormen', 'science', 'isbn104'),
(105, 'the catcher in the rye', 'j.d. salinger', 'fiction', 'isbn105');

insert into students (student_id, fname, lname, email, join_date) values
(1, 'alice', 'smith', 'alice@college.edu', '2023-01-15'),
(2, 'bob', 'jones', 'bob@college.edu', '2022-05-20'),
(3, 'charlie', 'brown', 'charlie@college.edu', '2020-01-01'), 
(4, 'david', 'wilson', 'david@college.edu', '2024-03-10');

insert into issues (book_id, student_id, issue_date, return_date) values
(101, 1, '2026-03-20', null),         
(102, 2, '2026-04-01', null),         
(103, 1, '2026-03-25', '2026-04-02'), 
(104, 4, '2026-03-10', null),         
(105, 2, '2026-02-15', '2026-03-01'); 

-- 1. penalty report for overdue books (more than 14 days)
select 
    s.fname, 
    s.lname, 
    b.title, 
    i.issue_date, 
    datediff(current_date, i.issue_date) as days_late
from issues i
join students s on i.student_id = s.student_id
join books b on i.book_id = b.book_id
where i.return_date is null 
and datediff(current_date, i.issue_date) > 14;

-- 2. showing most popular genres
select 
    category, 
    count(issue_id) as count
from issues i
join books b on i.book_id = b.book_id
group by category
order by count desc;

-- 3. cleaning up inactive students (no borrow in 3 years)
delete from students
where student_id not in (
    select distinct student_id 
    from issues 
    where issue_date > date_sub(current_date, interval 3 year)
)
and join_date < date_sub(current_date, interval 3 year);
