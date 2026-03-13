public class TypeCasting {
    public static void main(String[] args) {
        // Widening
        int myInt = 9;
        double myDouble = myInt; // Automatic
        
        // Narrowing
        double myDouble2 = 9.78d;
        int myInt2 = (int) myDouble2; // Manual
        
        System.out.println(myInt);
        System.out.println(myDouble);
        System.out.println(myDouble2);
        System.out.println(myInt2);
    }
}