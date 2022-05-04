import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Parser {
	public static double mass;
	public static double k;
	public static double gamma;
	public static double tf;
	public static double r0;
	public static double dt;


	public static void parse() throws FileNotFoundException, IOException, ParseException {
		JSONParser parser = new JSONParser();
		JSONObject data = (JSONObject) parser.parse(new FileReader("tp4/config.json"));

		mass=Double.parseDouble(data.get("mass").toString());
		k=Double.parseDouble(data.get("k").toString());
		k=Math.pow(10, k);
		gamma=Double.parseDouble(data.get("gamma").toString());
		tf=Double.parseDouble(data.get("tf").toString());
		r0=Double.parseDouble(data.get("r0").toString());
		dt=Double.parseDouble(data.get("dt").toString());
	}
}
