interface Sayable { void say(); }
public class MethodReferenceDemo {
    public static void saySomething() { System.out.println("Hello, this is static method."); }
    public static void main(String[] args) {
        Sayable sayable = MethodReferenceDemo::saySomething;
        sayable.say();
    }
}