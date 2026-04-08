public class EncapsulationExample {
    public static void main(String[] args) {
        Dog myDog = new Dog("Buddy", 3);
        myDog.bark();
        System.out.println("My dog is " + myDog.getAge() + " years old.");
    }
}