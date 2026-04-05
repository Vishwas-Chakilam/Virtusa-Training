enum TrafficLight { RED, YELLOW, GREEN }
public class TrafficLightDemo {
    public static void main(String[] args) {
        TrafficLight light = TrafficLight.RED;
        switch(light) {
            case RED: System.out.println("STOP"); break;
            case YELLOW: System.out.println("WAIT"); break;
            case GREEN: System.out.println("GO"); break;
        }
    }
}