package duplicates;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/**
 * Report generates a report including how many duplicates were removed and how many questions were renumbered
 * during the running of {@link Assessment#findDuplicates()}.
 * The number of renumberings can be jarring upon first site,
 * but feelings are subsided when reminded that if a question from early in the file is removed,
 * every question after that must be renumbered.
 * <p>
 * This class is a singleton due to the many-to-one nature of the problem;
 * several instances of Assessment (82 at the time of writing) are all writing to the same file.
 */
public class Report {

    private BufferedWriter writer;
    // decoration ~ "+----+----------+---+" to make the output table look pretty
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
            writer = new BufferedWriter(new FileWriter("./DuplicateDetective/src/main/reports/report.txt"));
            writer.write(decoration);
            writer.write(String.format("| %-73s | %10s | %10s |\n", "File", "Duplicates", "Renumbered"));
            writer.write(decoration);
            writer.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Called after an {@link Assessment} has removed duplicates and renumbered questions.
     * Writes to the file the name of the file, duplicate count, and renumber count.
     * Also adds to the total of these values for a "Total" row at the end of the file.
     *
     * @param a Assessment to get statistics from
     */
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

    /**
     * Writes the total statistics to the file and closes the writer.
     */
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
