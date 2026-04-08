public class GCDemo {
    public void finalize() {
        System.out.println("Garbage collected");
    }
    public static void main(String[] args) {
        GCDemo obj1 = new GCDemo();
        obj1 = null; // object is available for GC
        System.gc(); // Explicit request
    }
}