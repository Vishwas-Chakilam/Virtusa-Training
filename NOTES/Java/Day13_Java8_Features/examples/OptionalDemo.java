import java.util.Optional;

public class OptionalDemo {
    public static void main(String[] args) {
        String[] words = new String[10];
        words[5] = "hello";
        
        Optional<String> checkNull = Optional.ofNullable(words[5]);
        if(checkNull.isPresent()) {
            System.out.println("Word is: " + words[5]);
        }
        
        Optional<String> emptyCheck = Optional.ofNullable(words[0]);
        System.out.println("Is present? " + emptyCheck.isPresent()); // false
    }
}