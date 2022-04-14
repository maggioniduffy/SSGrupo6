import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        File out = new File("output.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("output.txt");
        Board board = new Board(5, 50);
        BrownianMovement bm = new BrownianMovement(board, writer);
        bm.start();
        writer.close();
    }
}
