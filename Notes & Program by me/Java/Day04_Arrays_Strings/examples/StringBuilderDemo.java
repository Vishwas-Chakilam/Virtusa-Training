public class StringBuilderDemo {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Hello");
        sb.append(" ");
        sb.append("Java!");
        System.out.println(sb.toString());
        sb.reverse();
        System.out.println("Reversed: " + sb.toString());
    }
}