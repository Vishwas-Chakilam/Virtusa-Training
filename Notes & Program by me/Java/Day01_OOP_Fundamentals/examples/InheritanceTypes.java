class Grandparent { void printGrandparent() { System.out.println("Grandparent"); } }
class Parent extends Grandparent { void printParent() { System.out.println("Parent"); } }
class Child1 extends Parent { void printChild1() { System.out.println("Child 1"); } }
class Child2 extends Parent { void printChild2() { System.out.println("Child 2"); } }

public class InheritanceTypes {
    public static void main(String[] args) {
        // Multilevel
        Child1 c1 = new Child1();
        c1.printGrandparent();
        c1.printParent();
        c1.printChild1();
        
        // Hierarchical
        Child2 c2 = new Child2();
        c2.printGrandparent();
        c2.printParent();
        c2.printChild2();
    }
}