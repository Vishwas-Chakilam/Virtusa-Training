public class ControlFlowDemo {
    public static void main(String[] args) {
        int target = 5;
        for(int i = 0; i < 10; i++) {
            if(i == target) {
                System.out.println("Target hit!");
                break;
            }
            System.out.println("Iteration: " + i);
        }
    }
}