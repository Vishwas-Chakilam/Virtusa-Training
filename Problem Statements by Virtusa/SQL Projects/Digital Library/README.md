# 📚 Digital Library Audit System

A relational database solution designed for community colleges to streamline book tracking, identify overdue loans, and analyze genre popularity to drive data-informed purchasing decisions.

---

## 🏛️ Database Schema
The system is built on a relational architecture featuring three core tables:
- **`Books`**: Catalog of items including title, author, and category.
- **`Students`**: Profile information for all library members.
- **`IssuedBooks`**: Transactional records tracking loan dates and returns.

## 📋 Key Audit Features

### 1. Penalty & Overdue Tracking
Automatically identifies students who have exceeded the **14-day borrowing limit**. The system calculates:
- Exact days overdue.
- List of unreturned items per student.

### 2. Genre Popularity Index
Uses aggregation techniques (`COUNT` and `GROUP BY`) to rank book categories. This helps librarians understand which genres (e.g., *Fiction*, *Science*, *History*) are most targeted by students.

### 3. Database Maintenance (Cleanup)
Includes logic to prune inactive student records. Any account with **no activity for over 3 years** is flagged and removed to maintain database performance and data relevance.

---

## 📂 Deliverables
- [DigitalLibrary.sql](file:///d:/Virtusa-Training/Virtusa-PreOnboarding-Training/Problem%20Statements%20by%20Virtusa/SQL/Digital%20Library/DigitalLibrary.sql): Contains the complete **DDL** (Table Creation), **DML** (Sample Records), and the **Analytical Queries**.

---

## 🛠️ How to Use
1. Import the `DigitalLibrary.sql` file into your preferred SQL environment (MySQL, PostgreSQL, etc.).
2. Run the DDL section to build the schema.
3. Execute the analytical queries to generate real-time library insights.