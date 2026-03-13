public class ThreadRace {
    public static void main(String[] args) {
        Runnable r = () -> {
            for(int i=1; i<=5; i++) {
                System.out.println(Thread.currentThread().getName() + " : " + i);
                try { Thread.sleep(100); } catch (InterruptedException e) {}
            }
        };
        Thread t1 = new Thread(r, "Thread-1");
        Thread t2 = new Thread(r, "Thread-2");
        t1.start();
        t2.start();
    }
}