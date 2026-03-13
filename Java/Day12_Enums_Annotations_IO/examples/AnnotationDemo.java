class Animal {
    public void displayInfo() { System.out.println("I am an animal."); }
}
class Bird extends Animal {
    @Override
    public void displayInfo() { System.out.println("I am a bird."); }
    
    @Deprecated
    public void oldMethod() { System.out.println("This is deprecated."); }
}
public class AnnotationDemo {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Bird b = new Bird();
        b.displayInfo();
        b.oldMethod(); // Suppressed warning
    }
}