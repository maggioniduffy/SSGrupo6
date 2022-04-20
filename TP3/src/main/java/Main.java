import org.json.simple.parser.ParseException;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
        File out = new File("output.txt");
        File vel = new File("speeds.txt");
        out.createNewFile();
        vel.createNewFile();
        FileWriter writer = new FileWriter("output.txt");
        FileWriter velWriter = new FileWriter("speeds.txt");
        Board board = new Board(Parser.v, Parser.N);
        BrownianMovement bm = new BrownianMovement(board, writer, velWriter);
        bm.start();
        writer.close();
    }
}
