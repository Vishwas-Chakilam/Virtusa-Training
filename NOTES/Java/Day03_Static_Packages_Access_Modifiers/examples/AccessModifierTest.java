class A {
    protected void msg() { System.out.println("Hello from protected method"); }
}
public class AccessModifierTest extends A {
    public static void main(String[] args) {
        AccessModifierTest obj = new AccessModifierTest();
        obj.msg(); // Accessible because of inheritance
    }
}