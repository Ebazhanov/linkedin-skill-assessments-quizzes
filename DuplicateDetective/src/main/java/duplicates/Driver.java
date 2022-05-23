package duplicates;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    static Scanner IN = new Scanner(System.in);

    public static void main(String[] args) {
        ArrayList<Assessment> assessments = loadAssessments();
        for (Assessment assessment : assessments) {
            assessment.findDuplicates();
            assessment.writeFile();
        }
        Report.getInstance().finish();
    }

    /**
     * Loads all quiz files and sends them to their own {@link Assessment} class.
     *
     * @return Quiz files represented by {@link Assessment} objects
     */
    static ArrayList<Assessment> loadAssessments() {
        ArrayList<Assessment> assessments = new ArrayList<>();
        // The search begins in the root directory, which contains a lot of directories, which then contain the quiz markdown files.
        File[] directories = new File("./").listFiles();
        if (directories != null) {
            for (File dir : directories) {
                if (dir.isDirectory()) {
                    File[] quizzes = dir.listFiles();
                    if (quizzes != null) {
                        for (File file : quizzes) {
                            if (file.getName().endsWith(".md")) {
                                assessments.add(new Assessment(file));
                            }
                        }
                    } else {
                        System.out.println("Could not find any files to examine in directory " + dir.getName() + "!");
                    }
                }
            }
        } else {
            System.out.println("Could not find any directories to examine!");
        }
        return assessments;
    }
}
