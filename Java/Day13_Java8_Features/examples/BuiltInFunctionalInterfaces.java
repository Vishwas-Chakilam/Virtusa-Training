import java.util.function.*;
public class BuiltInFunctionalInterfaces {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        System.out.println("Predicate (8 is even?): " + isEven.test(8));
        
        Function<Integer, Integer> square = n -> n * n;
        System.out.println("Function (5 squared): " + square.apply(5));
        
        Consumer<String> printer = s -> System.out.println("Consumer: " + s);
        printer.accept("Hello");
        
        Supplier<Double> randomValue = () -> Math.random();
        System.out.println("Supplier (Random): " + randomValue.get());
    }
}