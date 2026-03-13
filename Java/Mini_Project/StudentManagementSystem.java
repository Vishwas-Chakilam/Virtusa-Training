import java.util.*;

class Student {
    private int id;
    private String name;
    private double grade;

    public Student(int id, String name, double grade) {
        this.id = id;
        this.name = name;
        this.grade = grade;
    }
    public int getId() { return id; }
    public String getName() { return name; }
    public double getGrade() { return grade; }
    
    @Override
    public String toString() {
        return "ID: " + id + " | Name: " + name + " | Grade: " + grade;
    }
}

public class StudentManagementSystem {
    private Map<Integer, Student> db = new HashMap<>();

    public void addStudent(Student s) {
        db.put(s.getId(), s);
        System.out.println("Student Added Successfully.");
    }
    public void deleteStudent(int id) {
        if (db.remove(id) != null) System.out.println("Student Removed.");
        else System.out.println("Student Not Found.");
    }
    public void viewAll() {
        if(db.isEmpty()) { System.out.println("No Records."); return; }
        db.values().stream()
            .sorted(Comparator.comparing(Student::getName))
            .forEach(System.out::println);
    }

    public static void main(String[] args) {
        StudentManagementSystem sms = new StudentManagementSystem();
        sms.addStudent(new Student(101, "Alice", 92.5));
        sms.addStudent(new Student(102, "Bob", 88.0));
        sms.viewAll();
        sms.deleteStudent(101);
    }
}