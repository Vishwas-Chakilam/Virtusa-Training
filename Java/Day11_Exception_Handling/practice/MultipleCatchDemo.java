public class MultipleCatchDemo {
    public static void main(String[] args) {
        try {
            String s = null;
            System.out.println(s.length()); // Throws NullPointerException
        } catch(ArithmeticException e) {
            System.out.println("Arithmetic Exception occurs");
        } catch(ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBounds Exception occurs");
        } catch(Exception e) {
            System.out.println("Parent Exception occurs: " + e);
        }
    }
}