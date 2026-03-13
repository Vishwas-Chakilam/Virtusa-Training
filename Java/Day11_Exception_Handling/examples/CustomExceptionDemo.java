class InvalidAgeException extends Exception {
    InvalidAgeException(String s) {
        super(s);
    }
}
public class CustomExceptionDemo {
    static void validate(int age) throws InvalidAgeException {
        if(age < 18) throw new InvalidAgeException("Not valid to vote");
        else System.out.println("Welcome to vote");
    }
    public static void main(String[] args) {
        try {
            validate(13);
        } catch (Exception m) {
            System.out.println("Exception occurred: " + m);
        }
    }
}