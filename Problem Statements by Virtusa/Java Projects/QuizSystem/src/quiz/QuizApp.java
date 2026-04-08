package quiz;

import javax.swing.*;
import java.awt.*;
import java.util.List;

public class QuizApp extends JFrame {
    private QuizManager manager;
    private List<Question> qList;
    private int qNum = 0; // current question number
    private int score = 0;
    private int seconds = 30; // timer
    private Timer gameTimer;

    // GUI stuff
    private JLabel qArea;
    private JRadioButton[] opts = new JRadioButton[4];
    private ButtonGroup group;
    private JButton btnNext;
    private JLabel tLabel;
    private JProgressBar pBar;

    // colors for the dark theme
    private Color bg = new Color(33, 37, 41);
    private Color cardBg = new Color(52, 58, 64);
    private Color blueBtn = new Color(13, 110, 253);

    public QuizApp() {
        manager = new QuizManager();
        qList = manager.getAll();

        setTitle("Simple Java Quiz App");
        setSize(800, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        getContentPane().setBackground(bg);
        setLayout(new BorderLayout());

        buildUI();
        displayQ();
        runTimer();
    }

    private void buildUI() {
        // top part with timer
        JPanel top = new JPanel(new BorderLayout());
        top.setBackground(bg);
        top.setBorder(BorderFactory.createEmptyBorder(20, 20, 10, 20));

        tLabel = new JLabel("Time: 30s", JLabel.RIGHT);
        tLabel.setForeground(new Color(255, 193, 7));
        tLabel.setFont(new Font("Arial", Font.BOLD, 16));
        top.add(tLabel, BorderLayout.EAST);

        JLabel head = new JLabel("Online Quiz System", JLabel.LEFT);
        head.setForeground(Color.WHITE);
        head.setFont(new Font("Arial", Font.BOLD, 20));
        top.add(head, BorderLayout.WEST);

        add(top, BorderLayout.NORTH);

        // progress bar under header
        pBar = new JProgressBar(0, 30);
        pBar.setValue(30);
        pBar.setForeground(new Color(40, 167, 69));
        pBar.setBackground(cardBg);
        pBar.setBorderPainted(false);
        pBar.setPreferredSize(new Dimension(800, 5));
        top.add(pBar, BorderLayout.SOUTH);

        // middle card for question
        JPanel mid = new JPanel(new GridBagLayout());
        mid.setBackground(bg);
        
        JPanel card = new JPanel();
        card.setLayout(new BoxLayout(card, BoxLayout.Y_AXIS));
        card.setBackground(cardBg);
        card.setBorder(BorderFactory.createEmptyBorder(30, 40, 30, 40));
        card.setPreferredSize(new Dimension(650, 300));

        qArea = new JLabel("Loading...");
        qArea.setForeground(Color.WHITE);
        qArea.setFont(new Font("Arial", Font.PLAIN, 18));
        card.add(qArea);
        card.add(Box.createRigidArea(new Dimension(0, 30)));

        group = new ButtonGroup();
        for (int i = 0; i < 4; i++) {
            opts[i] = new JRadioButton();
            opts[i].setForeground(Color.LIGHT_GRAY);
            opts[i].setBackground(cardBg);
            opts[i].setFocusPainted(false);
            group.add(opts[i]);
            card.add(opts[i]);
            card.add(Box.createRigidArea(new Dimension(0, 10)));
        }

        mid.add(card);
        add(mid, BorderLayout.CENTER);

        // bottom buttons
        JPanel bottom = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        bottom.setBackground(bg);
        bottom.setBorder(BorderFactory.createEmptyBorder(10, 20, 30, 20));

        JButton adm = new JButton("Add Questions");
        styleMe(adm, new Color(108, 117, 125));
        adm.addActionListener(e -> openAdmin());
        bottom.add(adm);

        btnNext = new JButton("Next Step");
        styleMe(btnNext, blueBtn);
        btnNext.addActionListener(e -> clickNext());
        bottom.add(btnNext);

        add(bottom, BorderLayout.SOUTH);
    }

    private void styleMe(JButton b, Color c) {
        b.setBackground(c);
        b.setForeground(Color.WHITE);
        b.setFocusPainted(false);
        b.setBorder(BorderFactory.createEmptyBorder(10, 25, 10, 25));
    }

    private void displayQ() {
        if (qNum >= qList.size()) {
            report();
            return;
        }

        Question q = qList.get(qNum);
        qArea.setText("<html><body style='width: 500px'>" + (qNum + 1) + ". " + q.getText() + "</body></html>");
        String[] s = q.getChoices();
        for (int i = 0; i < 4; i++) {
            opts[i].setText(s[i]);
            opts[i].setSelected(false);
        }
        seconds = 30;
        pBar.setValue(30);
    }

    private void runTimer() {
        gameTimer = new Timer(1000, e -> {
            seconds--;
            pBar.setValue(seconds);
            tLabel.setText("Time: " + seconds + "s");
            if (seconds <= 0) {
                clickNext();
            }
        });
        gameTimer.start();
    }

    private void clickNext() {
        // checking the picked answer
        Question q = qList.get(qNum);
        for (int i = 0; i < 4; i++) {
            if (opts[i].isSelected() && i == q.getCorrect()) {
                score++;
            }
        }

        qNum++;
        if (qNum < qList.size()) {
            displayQ();
        } else {
            gameTimer.stop();
            report();
        }
    }

    private void report() {
        JOptionPane.showMessageDialog(this, "Quiz over! Your score: " + score + " / " + qList.size());
        System.exit(0);
    }

    private void openAdmin() {
        JTextField f1 = new JTextField();
        JTextField a1 = new JTextField();
        JTextField a2 = new JTextField();
        JTextField a3 = new JTextField();
        JTextField a4 = new JTextField();
        JTextField correct = new JTextField();

        Object[] msg = {"Question:", f1, "Choice 1:", a1, "Choice 2:", a2, "Choice 3:", a3, "Choice 4:", a4, "Correct (0-3):", correct};

        int r = JOptionPane.showConfirmDialog(null, msg, "New Question", JOptionPane.OK_CANCEL_OPTION);
        if (r == JOptionPane.OK_OPTION) {
            try {
                String[] cArr = {a1.getText(), a2.getText(), a3.getText(), a4.getText()};
                manager.addNew(new Question(f1.getText(), cArr, Integer.parseInt(correct.getText())));
                JOptionPane.showMessageDialog(this, "Added!");
            } catch (Exception ex) {}
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new QuizApp().setVisible(true));
    }
}
