package duplicates;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Report {
    private BufferedWriter writer;
    private final String decoration = "+" + "-".repeat(75) + "+" + "-".repeat(12) + "+" + "-".repeat(12) + "+\n";
    long duplicates = 0;
    long renumbered = 0;

    private static Report instance;

    static Report getInstance() {
        if (instance == null) {
            instance = new Report();
        }
        return instance;
    }

    private Report() {
        try {
            writer = new BufferedWriter(new FileWriter("./report.txt"));
            writer.write(decoration);
            writer.write(String.format("| %-73s | %10s | %10s |\n", "File", "Duplicates", "Renumbered"));
            writer.write(decoration);
            writer.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void add(Assessment a) {
        try {
            writer.write(String.format("| %-73s | %10d | %10d |\n", a.heading, a.dupCount, a.renumCount));
            writer.flush();
            duplicates += a.dupCount;
            renumbered += a.renumCount;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void finish() {
        try {
            writer.write(decoration);
            writer.write(String.format("| %-73s | %10d | %10d |\n", "Total", duplicates, renumbered));
            writer.write(decoration);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
