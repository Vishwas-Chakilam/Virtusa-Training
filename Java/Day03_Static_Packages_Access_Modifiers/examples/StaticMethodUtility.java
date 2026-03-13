public class StaticMethodUtility {
    // Static method
    public static int cube(int x) {
        return x * x * x;
    }
    
    public static void main(String[] args) {
        int result = StaticMethodUtility.cube(5);
        System.out.println("Cube of 5 is: " + result);
    }
}