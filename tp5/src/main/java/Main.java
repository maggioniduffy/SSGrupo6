import org.json.simple.parser.ParseException;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
/*
        SiloDischarge silo = new SiloDischarge(Parser.kn, 2*Parser.kn, Parser.L, Parser.W, Parser.D, Parser.dt);
        System.out.println(silo.getN());
        silo.simulate();

        //D: 0.1, 0.15, 0.18, 0.22
        //kt: 0.5kn, kn, 2kn, 3kn
        //Caudal: Nro. de Partículas que salieron en Dt / Dt

        File out = new File("caudal015.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("caudal015.txt");
        //writer.write(silo.getInitial_particles() + " " + silo.getRad_prom() + "\n");
        writer.write("D:" + Parser.D + "\n");
        ArrayList<Double> outTimes = silo.getOutTimes();
        for(int i = 0; i < outTimes.size()-49 ; i++){
            writer.write( (50.0/(outTimes.get(i+49)-outTimes.get(i))) + "\n");
        }
        writer.close();

        ArrayList<Double> kinetics = silo.getKinetics();
        File out = new File("kinetic3kn.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("kinetic3kn.txt");

        writer.write("kt: 3kn" + "\n");
        for (Double kinetic : kinetics) {
            writer.write( kinetic + "\n");
        }
        writer.close();
*/

        double[] diams = { 0.15, 0.18, 0.20, 0.22};
        int iteration = 1;
        int totalIterations = diams.length;
        for(double diam : diams){
            SiloDischarge silo = new SiloDischarge(Parser.kn, 0.5*Parser.kn, Parser.L, diam,  Parser.W, Parser.H, Parser.dt, iteration++, totalIterations);
//            System.out.println(silo.getN());
            silo.simulate();

            //D: 0.1, 0.12, 0.15, 0.18
            //kt: 0.5kn, kn, 2kn, 3kn
            //Caudal: Nro. de Partículas que salieron en Dt / Dt

            File out = new File("caudal0" + (int)(diam*100) + ".txt");
            out.createNewFile();
            FileWriter writer = new FileWriter("caudal0" + (int)(diam*100) + ".txt");
            writer.write(silo.getInitial_particles() + " " + silo.getRad_prom() + "\n");
            writer.write("D:" + diam+ "\n");
            ArrayList<Double> outTimes = silo.getOutTimes();
            for (Double outTime : outTimes) {
                writer.write( outTime + "\n");
            }
            writer.close();

            ArrayList<Double> kinetics = silo.getKinetics();
            out = new File("kinetic0" + (int)(diam*100) + ".txt");
            out.createNewFile();
            writer = new FileWriter("kinetic0" + (int)(diam*100) + ".txt");

            writer.write("D:" + diam + "\n");
            for (Double kinetic : kinetics) {
                writer.write( kinetic + "\n");
            }
            writer.close();
        }

    }
}
