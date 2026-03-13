public class GenericMethodDemo {
    public static <E> void printArray(E[] inputArray) {
        for(E element : inputArray) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Integer[] intArray = {1, 2, 3, 4, 5};
        String[] strArray = {"A", "B", "C"};
        
        System.out.print("Int array: "); printArray(intArray);
        System.out.print("Str array: "); printArray(strArray);
    }
}