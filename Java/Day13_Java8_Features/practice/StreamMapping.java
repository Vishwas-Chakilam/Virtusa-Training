import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamMapping {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("Java", "Stream", "API");
        List<Integer> lengths = words.stream()
            .map(String::length)
            .collect(Collectors.toList());
        System.out.println("Lengths: " + lengths);
    }
}