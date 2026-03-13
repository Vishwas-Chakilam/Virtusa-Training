public class CounterStaticDemo {
    static int count = 0; // memory allocated once
    
    CounterStaticDemo() {
        count++;
        System.out.println(count);
    }
    
    public static void main(String[] args) {
        CounterStaticDemo c1 = new CounterStaticDemo();
        CounterStaticDemo c2 = new CounterStaticDemo();
        CounterStaticDemo c3 = new CounterStaticDemo();
    }
}