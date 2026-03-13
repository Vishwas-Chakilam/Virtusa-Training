import java.util.*;
public class HashSetTreeSetDemo {
    public static void main(String[] args) {
        Set<String> hashSet = new HashSet<>(); // Unordered
        hashSet.add("Ravi");
        hashSet.add("Vijay");
        hashSet.add("Ravi"); // Ignores duplicate
        
        Set<String> treeSet = new TreeSet<>(); // Ordered
        treeSet.add("Ravi");
        treeSet.add("Vijay");
        treeSet.add("Ajay");
        
        System.out.println("HashSet (Unordered): " + hashSet);
        System.out.println("TreeSet (Sorted): " + treeSet);
    }
}