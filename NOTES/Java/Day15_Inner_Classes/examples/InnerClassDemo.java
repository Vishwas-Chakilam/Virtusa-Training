class Outer {
    private int data = 30;
    class Inner {
        void msg() { System.out.println("Data is " + data); }
    }
}
public class InnerClassDemo {
    public static void main(String[] args) {
        Outer obj = new Outer();
        Outer.Inner in = obj.new Inner();
        in.msg();
    }
}