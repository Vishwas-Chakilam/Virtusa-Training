public class BitwiseOperators {
    public static void main(String[] args) {
        int a = 5; // 0101
        int b = 7; // 0111
        System.out.println("a&b = " + (a & b)); // 0101 (5)
        System.out.println("a|b = " + (a | b)); // 0111 (7)
        System.out.println("a^b = " + (a ^ b)); // 0010 (2)
        System.out.println("~a = " + ~a);
    }
}