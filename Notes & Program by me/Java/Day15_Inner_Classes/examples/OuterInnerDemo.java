class Outer {
    int x = 10;
    class Inner {
        public int returnX() {
            return x; // accessing outer class variable
        }
    }
}
public class OuterInnerDemo {
    public static void main(String[] args) {
        Outer myOuter = new Outer();
        Outer.Inner myInner = myOuter.new Inner();
        System.out.println(myInner.returnX());
    }
}