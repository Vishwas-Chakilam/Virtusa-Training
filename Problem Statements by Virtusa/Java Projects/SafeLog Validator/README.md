# 🛡️ SafeLog: Corporate Password Validator

A modular cybersecurity utility built in **Core Java** to enforce strict employee password policies. The system provides granular feedback rather than binary results, helping users understand specific security gaps.

---

## 🔒 Security Policy
To ensure maximum protection, all passwords must meet the following criteria:
1.  **Length Requirement**: Minimum of **8 characters**.
2.  **Casing**: At least one **Uppercase letter** (A-Z).
3.  **Numerical**: At least one **Digit** (0-9).

---

## 🛠️ Technical Implementation
This project demonstrates several core programming concepts:
- **String Manipulation**: Using `.charAt()` and `Character` utility methods for deep string analysis.
- **Iteration**: A `for` loop efficiently traverses the string exactly once to check all conditions.
- **Conditional Feedback**: A custom feedback builder providing specific error messages (e.g., "Missing a digit").
- **Retry Mechanism**: A `while` loop maintains an interactive session until security standards are met.

---

## 📂 Deliverables
- [PasswordValidator.java](file:///d:/Virtusa-Training/Virtusa-PreOnboarding-Training/Problem%20Statements%20by%20Virtusa/Java/SafeLog%20Validator/PasswordValidator.java): The complete, standalone source code.

---

## 🏃 How to Run
1. Open your terminal in this directory.
2. Compile the source file:
   ```bash
   javac PasswordValidator.java
   ```
3. Run the validator:
   ```bash
   java PasswordValidator
   ```
