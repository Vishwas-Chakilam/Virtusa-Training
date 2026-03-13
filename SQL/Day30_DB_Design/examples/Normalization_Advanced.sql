-- Normalization example breaking down partial dependencies (2NF)
-- Original: CourseRegistry(StudentID, CourseID, StudentName, CourseName)
-- Partial Dependency: CourseName depends only on CourseID, StudentName only on StudentID.

-- Properly Normalized (3NF):
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100)
);

CREATE TABLE Enrollments (
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);