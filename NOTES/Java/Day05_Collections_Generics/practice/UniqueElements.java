import java.util.HashSet;
import java.util.Set;

public class UniqueElements {
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 4, 4, 5};
        Set<Integer> uniqueNums = new HashSet<>();
        for(int n : nums) {
            uniqueNums.add(n);
        }
        System.out.println("Unique Elements: " + uniqueNums);
    }
}