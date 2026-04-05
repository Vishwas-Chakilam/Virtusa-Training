import java.util.ArrayList;
import java.util.List;

public class OutOfMemorySimulator {
    // Run with small heap e.g., java -Xmx10m OutOfMemorySimulator
    public static void main(String[] args) {
        List<byte[]> memoryHog = new ArrayList<>();
        try {
            while(true) {
                // Keep allocating 1MB chunks
                memoryHog.add(new byte[1048576]);
            }
        } catch(OutOfMemoryError e) {
            System.err.println("Max Heap reached! OutOfMemoryError Caught!");
        }
    }
}