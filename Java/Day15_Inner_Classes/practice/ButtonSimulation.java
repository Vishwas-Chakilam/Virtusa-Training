interface ClickListener {
    void onClick();
}

class Button {
    ClickListener listener;
    public void setOnClickListener(ClickListener listener) {
        this.listener = listener;
    }
    public void click() {
        if(listener != null) listener.onClick();
    }
}

public class ButtonSimulation {
    public static void main(String[] args) {
        Button btn = new Button();
        btn.setOnClickListener(new ClickListener() {
            public void onClick() {
                System.out.println("Button was clicked using Anonymous Inner Class!");
            }
        });
        btn.click();
    }
}