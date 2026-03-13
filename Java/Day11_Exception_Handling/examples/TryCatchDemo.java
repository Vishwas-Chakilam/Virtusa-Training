public class TryCatchDemo {
    public static void main(String[] args) {
        try {
            int data = 100 / 0; // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Exception handled: " + e);
        }
        System.out.println("Rest of the code...");
    }
}