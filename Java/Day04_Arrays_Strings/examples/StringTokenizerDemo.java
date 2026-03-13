import java.util.StringTokenizer;
public class StringTokenizerDemo {
    public static void main(String[] args) {
        StringTokenizer st = new StringTokenizer("my name is string tokenizer"," ");
        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
    }
}