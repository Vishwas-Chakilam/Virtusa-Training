class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running from class extending Thread.");
    }
}
public class ThreadExtendDemo {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start(); // calls run() asynchronously
    }
}