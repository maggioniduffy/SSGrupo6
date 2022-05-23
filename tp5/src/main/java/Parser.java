import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Parser {

    public static double mass;

    public static void parse() throws FileNotFoundException, IOException, ParseException {
        JSONParser parser = new JSONParser();
        JSONObject data = (JSONObject) parser.parse(new FileReader("config.json"));

        mass=Double.parseDouble(data.get("mass").toString());
    }
}
