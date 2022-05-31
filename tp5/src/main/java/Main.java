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

        writer.write("D:" + Parser.D + "\n");
        ArrayList<Integer> outParticles = silo.getOutParticles();
        for (Integer i : outParticles) {
            writer.write( i + "\n");
        }
        writer.close();

        ArrayList<Double> kinetics = silo.getKinetics();
        out = new File("kinetic015.txt");
        out.createNewFile();
        writer = new FileWriter("kinetic015.txt");

        writer.write("D:" + Parser.D + "\n");
        for (Double kinetic : kinetics) {
            writer.write( kinetic + "\n");
        }
        writer.close();
    }
}
