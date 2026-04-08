package quiz;

import java.io.Serializable;

// this class just stores the data for each question
public class Question implements Serializable {
    private String text;
    private String[] choices;
    private int correct;

    public Question(String text, String[] choices, int correct) {
        this.text = text;
        this.choices = choices;
        this.correct = correct;
    }

    public String getText() {
        return text;
    }

    public String[] getChoices() {
        return choices;
    }

    public int getCorrect() {
        return correct;
    }
}
