public class ClassLoaderDemo {
    public static void main(String[] args) {
        Class c = ClassLoaderDemo.class;
        System.out.println(c.getClassLoader()); // AppClassLoader
        System.out.println(String.class.getClassLoader()); // null (Bootstrap ClassLoader)
    }
}