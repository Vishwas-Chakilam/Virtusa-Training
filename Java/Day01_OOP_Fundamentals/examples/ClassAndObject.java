class Car {
    String color;
    void drive() { System.out.println("Driving"); }
}
public class ClassAndObject {
    public static void main(String[] args) {
        Car myCar = new Car();
        myCar.color = "Red";
        myCar.drive();
    }
}
