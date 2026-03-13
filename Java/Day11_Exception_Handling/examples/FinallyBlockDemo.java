public class FinallyBlockDemo {
    public static void main(String[] args) {
        try {
            int[] arr = new int[2];
            arr[3] = 5; // Array out of bounds
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index out of bound!");
        } finally {
            System.out.println("Finally block is always executed");
        }
    }
}