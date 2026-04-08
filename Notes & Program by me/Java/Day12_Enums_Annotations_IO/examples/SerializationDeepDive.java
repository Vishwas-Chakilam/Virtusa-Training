import java.io.*;
class Student implements Serializable {
    transient int id; // transient will not be serialized
    String name;
    public Student(int id, String name) {
        this.id = id; this.name = name;
    }
}
public class SerializationDeepDive {
    public static void main(String args[]){
        try {
            Student s1 = new Student(211, "ravi");
            FileOutputStream fout = new FileOutputStream("f.txt");
            ObjectOutputStream out = new ObjectOutputStream(fout);
            out.writeObject(s1); out.flush(); out.close(); fout.close();
            
            ObjectInputStream in = new ObjectInputStream(new FileInputStream("f.txt"));
            Student s = (Student)in.readObject();
            System.out.println(s.id + " " + s.name); // id will be 0 due to transient
            in.close();
        } catch(Exception e) { System.out.println(e); }
    }
}