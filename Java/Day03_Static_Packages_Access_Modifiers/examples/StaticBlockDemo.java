public class StaticBlockDemo {
    static {
        System.out.println("Static block is invoked");
    }
    public static void main(String[] args) {
        System.out.println("Main method is invoked");
    }
}