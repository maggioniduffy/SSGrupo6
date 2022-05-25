import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.util.Random;

public class Main {
    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
        SiloDischarge silo = new SiloDischarge(Parser.kn, Parser.L, Parser.W, Parser.D, Parser.dt);
        System.out.println(silo.getN());

    }
}
