public class GarbageCollectionDemo {
    public void finalize() {
        System.out.println("Garbage Collection algorithm triggered! Object is being destroyed.");
    }
    public static void main(String[] args) {
        GarbageCollectionDemo obj1 = new GarbageCollectionDemo();
        GarbageCollectionDemo obj2 = new GarbageCollectionDemo();
        
        // Nulling references
        obj1 = null;
        obj2 = null;
        
        // Requesting JVM to perform GC
        System.gc();
    }
}