import java.util.Scanner;

public class PasswordValidator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String pw;
        boolean flag = false;

        System.out.println("--- Password Policy Checker ---");
        System.out.println("Your password must have:");
        System.out.println("1. 8 or more characters");
        System.out.println("2. At least one BIG letter (A-Z)");
        System.out.println("3. At least one number (0-9)\n");

        // keep asking until it's right
        while (!flag) {
            System.out.print("Enter password: ");
            pw = sc.nextLine();

            // string builder to collect errors
            StringBuilder errs = new StringBuilder();
            boolean up_found = false;
            boolean num_found = false;

            // checking length first
            if (pw.length() < 8) {
                errs.append("- Password is too short (min 8)\n");
            }

            // check each character
            for (int i = 0; i < pw.length(); i++) {
                char c = pw.charAt(i);
                if (Character.isUpperCase(c)) {
                    up_found = true;
                } else if (Character.isDigit(c)) {
                    num_found = true;
                }
            }

            if (!up_found) {
                errs.append("- You need at least one uppercase letter\n");
            }
            if (!num_found) {
                errs.append("- You need at least one number\n");
            }

            // check if everything is ok
            if (pw.length() >= 8 && up_found && num_found) {
                System.out.println("\nGreat! Password updated successfully.");
                flag = true;
            } else {
                System.out.println("\nInvalid password! See errors below:");
                System.out.print(errs.toString());
                System.out.println("---------------------------------");
            }
        }

        sc.close();
    }
}
