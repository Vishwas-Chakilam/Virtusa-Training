import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
class WorkerThread implements Runnable {
    private String message;
    public WorkerThread(String s){ this.message = s; }
    public void run() {
        System.out.println(Thread.currentThread().getName() + " (Start) " + message);
        try { Thread.sleep(500); } catch (Exception e) {}
        System.out.println(Thread.currentThread().getName() + " (End)");
    }
}
public class ThreadPoolDemo {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        for (int i = 0; i < 5; i++) {
            Runnable worker = new WorkerThread("" + i);
            executor.execute(worker);
        }
        executor.shutdown();
        while (!executor.isTerminated()) { }
        System.out.println("Finished all threads");
    }
}