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
        printReport(assessments);
    }

    static void printReport(ArrayList<Assessment> assessments) {
        String decoration = "+" + "-".repeat(75) + "+" + "-".repeat(12) + "+" + "-".repeat(12) + "+";
        long duplicates = 0;
        long renumbered = 0;
        System.out.println("Finished finding duplicates!");
        System.out.println("----- Report -----");
        System.out.println(decoration);
        System.out.printf("| %-73s | %10s | %10s |\n", "File", "Duplicates", "Renumbered");
        System.out.println(decoration);
        for (Assessment a : assessments) {
            System.out.printf("| %-73s | %10d | %10d |\n", a.heading, a.dupCount, a.renumCount);
            duplicates += a.dupCount;
            renumbered += a.renumCount;
        }
        System.out.println(decoration);
        System.out.printf("| %-73s | %10d | %10d |\n", "Total", duplicates, renumbered);
        System.out.println(decoration);
    }

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
