package quiz;

import java.util.ArrayList;
import java.util.List;

public class QuizManager {
    private List<Question> qList;

    public QuizManager() {
        qList = new ArrayList<>();
        initData();
    }

    // adding some starting questions
    private void initData() {
        qList.add(new Question(
            "What is the default value of a boolean variable in Java?",
            new String[]{"true", "false", "0", "null"},
            1
        ));
        qList.add(new Question(
            "Which concept in Java allows one class to acquire properties of another?",
            new String[]{"Polymorphism", "Encapsulation", "Inheritance", "Abstraction"},
            2
        ));
        qList.add(new Question(
            "What is the time complexity of searching an element in a balanced BST?",
            new String[]{"O(n)", "O(n log n)", "O(log n)", "O(1)"},
            2
        ));
    }

    public void addNew(Question q) {
        qList.add(q);
    }

    public List<Question> getAll() {
        return qList;
    }
}
