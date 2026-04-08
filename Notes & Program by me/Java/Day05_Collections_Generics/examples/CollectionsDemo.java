import java.util.*;
public class CollectionsDemo {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        for (String item : list) { System.out.println(item); }
        
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        System.out.println(map.get(1));
    }
}