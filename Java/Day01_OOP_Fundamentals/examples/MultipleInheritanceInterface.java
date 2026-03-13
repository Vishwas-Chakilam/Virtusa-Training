interface Flyable { void fly(); }
interface Swimmable { void swim(); }
class Duck implements Flyable, Swimmable {
    public void fly() { System.out.println("Duck flying"); }
    public void swim() { System.out.println("Duck swimming"); }
}
public class MultipleInheritanceInterface {
    public static void main(String[] args) {
        Duck d = new Duck();
        d.fly(); d.swim();
    }
}