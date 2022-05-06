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
    public static double k2;
    public static double Q;
    public static double M;
    public static double D;
    public static double N;
    public static double V0max;
    public static double V0min;


	public static void parse() throws FileNotFoundException, IOException, ParseException {
		JSONParser parser = new JSONParser();
		JSONObject data = (JSONObject) parser.parse(new FileReader("config.json"));

		//Sistema1
		mass=Double.parseDouble(data.get("mass").toString());
		k=Double.parseDouble(data.get("k").toString());
		k=Math.pow(10, k);
		gamma=Double.parseDouble(data.get("gamma").toString());
		tf=Double.parseDouble(data.get("tf").toString());
		r0=Double.parseDouble(data.get("r0").toString());
		dt=Double.parseDouble(data.get("dt").toString());
		//Sistema 2
        k2=Double.parseDouble(data.get("k2").toString());
        k2=Math.pow(10, k2);
        Q=Double.parseDouble(data.get("Q").toString());
        Q=Math.pow(10, Q);
        M=Double.parseDouble(data.get("M").toString());
        M=Math.pow(10, M);
        D=Double.parseDouble(data.get("D").toString());
        D=Math.pow(10, D);
        N=Double.parseDouble(data.get("N").toString());
        N=Math.pow(N, 2);
        V0max=Double.parseDouble(data.get("V0max").toString());
        V0min=Double.parseDouble(data.get("V0min").toString());

	}
}
