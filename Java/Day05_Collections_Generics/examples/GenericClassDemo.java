class Box<T> {
    private T item;
    public void set(T item) { this.item = item; }
    public T get() { return this.item; }
}

public class GenericClassDemo {
    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<>();
        integerBox.set(100);
        System.out.println("Integer Value: " + integerBox.get());
        
        Box<String> stringBox = new Box<>();
        stringBox.set("Generics are cool");
        System.out.println("String Value: " + stringBox.get());
    }
}