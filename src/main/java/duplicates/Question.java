package duplicates;

public record Question(int number, String prompt, String answer) {
    public String toString() {
        String question = "---- QUESTION ----\n";
        question += "Number: " + number + "\n";
        question += "Prompt:\n" + prompt;
        question += "Answer:\n" + answer;
        return question;
    }
}
