import java.util.concurrent.*;

class DownloadTask implements Runnable {
    private String file;
    public DownloadTask(String file) { this.file = file; }
    
    @Override
    public void run() {
        System.out.println("Starting download: " + file + " on " + Thread.currentThread().getName());
        try {
            Thread.sleep((long)(Math.random() * 2000));
        } catch(InterruptedException e) { e.printStackTrace(); }
        System.out.println("Completed download: " + file);
    }
}

public class MultithreadedDownloaderSim {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newFixedThreadPool(3);
        String[] files = {"image1.png", "video.mp4", "doc.pdf", "game.zip", "music.mp3"};
        
        for(String f : files) {
            pool.execute(new DownloadTask(f));
        }
        pool.shutdown();
        System.out.println("All tasks dispatched.");
    }
}