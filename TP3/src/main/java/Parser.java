import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Parser {
	public static int N;
	public static int v;


	public static void parse() throws FileNotFoundException, IOException, ParseException {
		JSONParser parser = new JSONParser();
		JSONObject data = (JSONObject) parser.parse(new FileReader("config.json"));

		v=Integer.parseInt(data.get("max_speed").toString());
		N=Integer.parseInt(data.get("quantity").toString());
	}
}
