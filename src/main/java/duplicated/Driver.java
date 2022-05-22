package duplicated;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Driver {
    static long times = 0;

    public static void main(String[] args) {
        File[] files = new File("./").listFiles();
        for (File dir : files) {
            if (dir.isDirectory()) {
                for (File file : dir.listFiles()) {
                    if (file.getName().endsWith(".md")) {
                        findDuplicates(file);
                    }
                }
            }
        }
        System.out.println("End of Report");
        System.out.println("Similarities: " + times);
    }

    static void findDuplicates(File file) {
        ArrayList<String> questions = loadQuestions(file);
        for (int i = 0; i < questions.size(); i++) {
            for (int j = i + 1; j < questions.size(); j++) {
                double similarity = similarity(questions.get(i), questions.get(j));
                if (similarity > 0.8) {
                    times++;
                    System.out.println("FOUND SIMILARITY");
                    System.out.println(questions.get(i));
                    System.out.println(questions.get(j));
                    System.out.println(similarity);
                }
            }
        }
    }

    static ArrayList<String> loadQuestions(File file) {
        ArrayList<String> questions = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.startsWith("####")) {
                    // Parse the full line into only the question
                    // Adds the substring of the line beginning at the second space.
                    questions.add(line.substring(line.indexOf(' ', line.indexOf(' ')) + 1));
                }
            }
            return questions;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return questions;
    }

    public static double similarity(String s1, String s2) {
        String longer = s1, shorter = s2;
        if (s1.length() < s2.length()) { // longer should always have greater length
            longer = s2;
            shorter = s1;
        }
        int longerLength = longer.length();
        if (longerLength == 0) {
            return 1.0; /* both strings are zero length */
        }
        return (longerLength - editDistance(longer, shorter)) / (double) longerLength;

    }

    public static int editDistance(String s1, String s2) {
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        int[] costs = new int[s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            int lastValue = i;
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0)
                    costs[j] = j;
                else {
                    if (j > 0) {
                        int newValue = costs[j - 1];
                        if (s1.charAt(i - 1) != s2.charAt(j - 1))
                            newValue = Math.min(Math.min(newValue, lastValue),
                                    costs[j]) + 1;
                        costs[j - 1] = lastValue;
                        lastValue = newValue;
                    }
                }
            }
            if (i > 0)
                costs[s2.length()] = lastValue;
        }
        return costs[s2.length()];
    }
}
