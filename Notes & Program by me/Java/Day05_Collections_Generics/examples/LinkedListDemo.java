import java.util.LinkedList;
public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> al = new LinkedList<>();
        al.add("Ravi");
        al.add("Vijay");
        al.addFirst("Lokesh");
        al.addLast("Harsh");
        System.out.println(al);
    }
}