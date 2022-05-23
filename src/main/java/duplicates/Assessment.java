package duplicates;

import java.io.*;
import java.util.ArrayList;

/**
 * An Assessment represents a file that contains a quiz.
 * All Assessments have a heading, and a list of questions.
 */
public class Assessment {

    private File file;
    private ArrayList<Question> questions;
    String heading, subheading;
    ArrayList<Question> dupQuestions;
    int dupCount, renumCount;

    Assessment(File file) {
        this.file = file;
        ArrayList<ArrayList<String>> blocks = generateBlocks(file);
        questions = new ArrayList<>();
        for (ArrayList<String> block : blocks) {
            questions.add(parseBlock(block));
        }
    }

    /**
     * Generates an ArrayList of blocks of text.
     * Blocks are just chunks of text that contain the question prompt and question answers.
     * This will be further parsed into the number, prompt, and answers in {@link #parseBlock(ArrayList)}.
     * This method also determines the heading of the file and any subheadings that are possibly under the heading.
     *
     * @param file File to be parsed into blocks
     * @return ArrayList of question text blocks
     */
    ArrayList<ArrayList<String>> generateBlocks(File file) {
        ArrayList<ArrayList<String>> blocks = new ArrayList<>();
        int lineNumber = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;
            // Block will hold one entire question. It will act like the `peek` variable of a normal parser.
            ArrayList<String> currentBlock = new ArrayList<>();
            while ((line = reader.readLine()) != null) {
                lineNumber++;
                // If this line starts with "## ", then it is the heading of a new file.
                // If this line starts with "> ", then it is a subheading
                // Let's store that separately.
                if ((line.startsWith("## ") || line.startsWith("\uFEFF")) && lineNumber == 1) {  // FEFF is a byte order mark that some Microsoft editors place at the beginning of the file.
                    int space = line.indexOf(' ');
                    heading = line.substring(space + 1);
                    // Heading is followed by a blank line, so skip it.
                    reader.readLine();
                    continue;
                } else if (line.startsWith("> ") && lineNumber == 2) {
                    subheading = line;
                    reader.readLine();
                    continue;
                } else if (line.startsWith("#### Q") && !currentBlock.isEmpty()) {
                    blocks.add(currentBlock);
                    currentBlock = new ArrayList<>();
                }
                currentBlock.add(line);
            }
            // Last question needs to be added!
            blocks.add(currentBlock);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return blocks;
    }

    /**
     * Parses a block of text into a Question.
     * Blocks have the following form:
     * <pre>
     * #### Q`number`. `prompt`
     * < possibly more text, such as code or image references >
     * `blank line`
     * `List of answers, beginning with "- ["`
     * `blank line`
     * </pre>
     *
     * @param block ArrayList of Strings representing the entire question (number, prompt, answer)
     * @return A Question object with everything separated.
     */
    Question parseBlock(ArrayList<String> block) {
        // Parse the prompt
        // First 6 characters are always "#### Q"
        String first = block.remove(0);
        int dot = first.indexOf('.');
        int number = Integer.parseInt(first.substring(6, dot));
        // Remove the number and space before prompt
        first = first.substring(dot + 2);
        // Gather the rest of the prompt, which is every line up to the first answer.
        StringBuilder prompt = new StringBuilder(first);
        while (!block.get(0).startsWith("- [")) {
            prompt.append("\n").append(block.remove(0));
        }
        // The rest of the array now just contains the answers.
        String answers = String.join("\n", block);
        return new Question(number, prompt.toString(), answers);
    }

    void findDuplicates() {
        dupQuestions = new ArrayList<>();
        System.out.println("---- Finding duplicates in " + heading + " ----");
        for (int i = 0; i < questions.size(); i++) {
            for (int j = i + 1; j < questions.size(); j++) {
                double similarity = Distance.similarity(questions.get(i).prompt(), questions.get(j).prompt());
                if (similarity > 0.8) {
                    System.out.println("-- VERSION 1 --");
                    System.out.println(questions.get(i));
                    System.out.println("-- VERSION 2 --");
                    System.out.println(questions.get(j));
                    System.out.printf("There is a %%%5.2f similarity. Are they duplicates? (y<optional: number>/n) \n", similarity * 100);
                    String answer = Driver.IN.nextLine();
                    boolean isDuplicate = answer.charAt(0) == 'y';
                    if (isDuplicate) {
                        // User has the option of choosing which to delete if there is a duplicate, and the number will come after y.
                        int num;
                        if (answer.length() != 1) {
                            num = Integer.parseInt(answer.substring(1));
                            if (questions.get(i).number() == num) {
                                dupQuestions.add(questions.get(i));
                            } else if (questions.get(j).number() == num) {
                                dupQuestions.add(questions.get(j));
                            } else {
                                //TODO This needs to ask for the number again. For now, aborting process will cancel answers to current file but previous files are saved.
                                System.err.println("That number is not valid! Removing largest number");
                            }
                        } else {
                            dupQuestions.add(questions.get(i).number() > questions.get(j).number() ? questions.get(i) : questions.get(j));
                        }
                    }
                    System.out.println("\n\n\n");
                }
            }
        }
        dupCount += dupQuestions.size();
        for (Question question : dupQuestions) {
            questions.remove(question);
        }
    }

    void writeFile() {
        int index = 1;
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write("## " + heading + '\n');
            if (subheading != null) {
                writer.write(subheading + '\n');
            }
            for (Question question : questions) {
                if (question.number() != index) {
                    renumCount++;
                }
                writer.write("#### Q" + index++ + ". " + question.prompt() + '\n');
                writer.write(question.answer() + '\n');
            }
            writer.flush();
            writer.close();
            Report.getInstance().add(this);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
