final class FinalClass {} // Cannot be inherited
class Parent {
    final void method() { System.out.println("Final method"); } // Cannot be overridden
}
public class FinalKeywordDemo extends Parent {
    public static void main(String[] args) {
        final int LIMIT = 90; // Cannot be changed
        System.out.println("Limit: " + LIMIT);
    }
}