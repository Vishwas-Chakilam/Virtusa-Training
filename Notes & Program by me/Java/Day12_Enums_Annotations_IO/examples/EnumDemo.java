enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
public class EnumDemo {
    public static void main(String[] args) {
        Day today = Day.WEDNESDAY;
        if(today == Day.WEDNESDAY) {
            System.out.println("It's Wednesday!");
        }
    }
}