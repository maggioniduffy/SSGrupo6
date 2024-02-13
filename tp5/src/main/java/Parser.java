import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Parser {

    public static double mass, kn, L, D, W, H, d, dt, gamma, wallgamma;

    public static void parse() throws FileNotFoundException, IOException, ParseException {
        JSONParser parser = new JSONParser();
        JSONObject data = (JSONObject) parser.parse(new FileReader("/home/rodri/SSGrupo6/tp5/config.json"));

        mass=Double.parseDouble(data.get("mass").toString());
        kn = Double.parseDouble(data.get("kn").toString());
        L = Double.parseDouble(data.get("L").toString());
        D = Double.parseDouble(data.get("D").toString());
        W = Double.parseDouble(data.get("W").toString());
        H = Double.parseDouble(data.get("H").toString());
        d = Double.parseDouble(data.get("d").toString());
        dt = Double.parseDouble(data.get("dt").toString());
        gamma = Double.parseDouble(data.get("gamma").toString());
        wallgamma = Double.parseDouble(data.get("wallgamma").toString());
    }
}
