import java.io.*;

public class FileIODemo {
    public static void main(String[] args) {
        try (FileWriter fw = new FileWriter("test.txt")) {
            fw.write("Java File I/O Example!");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}