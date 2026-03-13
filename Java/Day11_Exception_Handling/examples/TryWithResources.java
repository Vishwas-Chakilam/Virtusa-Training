import java.io.FileOutputStream;
public class TryWithResources {
    public static void main(String args[]) {
        try(FileOutputStream fileOutputStream = new FileOutputStream("abc.txt")){
            String msg = "Welcome to java";
            byte byteArray[] = msg.getBytes();
            fileOutputStream.write(byteArray);
            System.out.println("Message written to file successfuly!");
        } catch(Exception exception){
            System.out.println(exception);
        }
    }
}