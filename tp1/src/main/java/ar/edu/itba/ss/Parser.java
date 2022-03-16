package ar.edu.itba.ss;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Parser {
	static int N;
	static double L;
	static int M;
	static Set<Particle> particles = new TreeSet<Particle>();
	static boolean periodicContour;
	static double rc;
	static int method;
	
	
	public static void parse() throws FileNotFoundException, IOException, ParseException {
		JSONParser parser = new JSONParser();
		JSONObject data = (JSONObject) parser.parse(new FileReader("config.json"));
		
		//options
		periodicContour=(boolean) data.get("periodicContour");
		rc=Double.parseDouble(data.get("rc").toString());
		method=Integer.parseInt(data.get("method").toString());
		L=Double.parseDouble(data.get("L").toString());
		M=Integer.parseInt(data.get("M").toString());
		N=Integer.parseInt(data.get("N").toString());
		//static file
		
		String file = data.get("staticFile").toString();
        File f = new File(file);
        Scanner sc = new Scanner(f);
        N = sc.nextInt();
        L = sc.nextDouble();
        for (int i = 0; i < N; i++){
            double radius   = sc.nextDouble();
            sc.nextDouble();
            particles.add(new Particle(i, radius));
        }
        sc.close();
        
        // dynamic file 
        file = data.get("dynamicFile").toString();
        f = new File(file);
        Scanner dsc = new Scanner(f);
        dsc.nextInt();   /* Discard first time value */
        for (Particle p : particles){
            double x = dsc.nextDouble();
            double y = dsc.nextDouble();
        	p.setX(x);
            p.setY(y);
        }
    }
	
	
	
}
