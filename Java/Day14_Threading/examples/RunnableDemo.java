class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread running from class implementing Runnable.");
        try { Thread.sleep(1000); } catch(Exception e) {}
        System.out.println("Thread woke up!");
    }
}
public class RunnableDemo {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable());
        t.start();
    }
}