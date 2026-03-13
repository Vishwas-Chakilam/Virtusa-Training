public class ClassLoaderInfo {
    public static void main(String[] args) {
        // Application ClassLoader
        System.out.println(ClassLoaderInfo.class.getClassLoader()); 
        // Extension or Platform ClassLoader
        System.out.println(java.sql.DriverManager.class.getClassLoader());
        // Bootstrap ClassLoader (Usually prints null)
        System.out.println(String.class.getClassLoader()); 
    }
}