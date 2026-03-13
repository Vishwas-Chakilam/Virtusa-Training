public class StringDemo {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "Hello";
        System.out.println(s1 == s2); // true (String Pool)
        
        StringBuilder sb = new StringBuilder("Java");
        sb.append(" 17");
        System.out.println(sb.toString());
    }
}