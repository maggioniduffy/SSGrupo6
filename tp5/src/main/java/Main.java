import org.json.simple.parser.ParseException;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
        SiloDischarge silo = new SiloDischarge(Parser.kn, Parser.L, Parser.W, Parser.D, Parser.dt);
        System.out.println(silo.getN());
        silo.simulate();

        //D: 0.15, 0.18, 0.22, 0.25
        //L: 1, 1.5
        //W: 0.3, 0.4
        //Caudal: Nro. de Partículas que salieron en Dt / Dt

        File out = new File("caudal015.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("caudal015.txt");
        writer.write(silo.getInitial_particles() + " " + silo.getRad_prom() + "\n");
        writer.write("D:" + Parser.D + "\n");
        ArrayList<Double> outTimes = silo.getOutTimes();
        for(int i = 0; i < outTimes.size()-49 ; i++){
            writer.write( (50.0/(outTimes.get(i+49)-outTimes.get(i))) + "\n");
        }
        writer.close();

        ArrayList<Double> kinetics = silo.getKinetics();
        out = new File("kinetic025.txt");
        out.createNewFile();
        writer = new FileWriter("kinetic025.txt");

        writer.write("D:" + Parser.D + "\n");
        for (Double kinetic : kinetics) {
            writer.write( kinetic + "\n");
        }
        writer.close();
    }
}
