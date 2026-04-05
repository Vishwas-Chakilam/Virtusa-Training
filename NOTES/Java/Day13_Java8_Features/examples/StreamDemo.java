import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamDemo {
    public static void main(String[] args) {
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");
        // Filter out empty strings
        List<String> filtered = strings.stream()
            .filter(string -> !string.isEmpty())
            .collect(Collectors.toList());
            
        System.out.println("Filtered: " + filtered);
    }
}