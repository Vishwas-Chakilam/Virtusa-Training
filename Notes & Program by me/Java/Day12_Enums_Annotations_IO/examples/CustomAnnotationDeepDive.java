import java.lang.annotation.*;
import java.lang.reflect.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface MyCustomAnnotation {
    int value();
}

class Hello {
    @MyCustomAnnotation(value=10)
    public void sayHello() { System.out.println("hello annotation"); }
}

public class CustomAnnotationDeepDive {
    public static void main(String args[]) throws Exception {
        Hello h = new Hello();
        Method m = h.getClass().getMethod("sayHello");
        
        MyCustomAnnotation manno = m.getAnnotation(MyCustomAnnotation.class);
        System.out.println("value is: " + manno.value());
    }
}