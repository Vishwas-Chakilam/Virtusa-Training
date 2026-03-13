class Table {
    synchronized void printTable(int n) { // synchronized method
        for(int i=1; i<=5; i++) {
            System.out.println(n*i);
            try { Thread.sleep(400); } catch(Exception e) {}
        }
    }
}
public class SynchronizationDemo {
    public static void main(String[] args) {
        Table obj = new Table(); // shared object
        Thread t1 = new Thread(() -> obj.printTable(5));
        Thread t2 = new Thread(() -> obj.printTable(100));
        t1.start();
        t2.start();
    }
}