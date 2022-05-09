import org.json.simple.parser.ParseException;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
        //Sistema 1
        File out = new File("output.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("output.txt");
        Oscilator oscilator = new Oscilator(Parser.mass, Parser.k, Parser.gamma, Parser.tf, Parser.r0, Parser.dt);
        oscilator.solution();
        writer.write("Analytical:\n");
        ArrayList<Double> analytical = oscilator.getAnalytical();
        for(Double pos : analytical){
            writer.write(pos.toString() + "\n");
        }
        writer.write("Verlet:\n");
        ArrayList<PosVel> verlet = oscilator.getVerlet();
        verlet.remove(0);
        for(PosVel pos : verlet){
            writer.write(pos.getPosition() + "\n");
        }
        writer.write("Beeman:\n");
        ArrayList<PosVel> beeman = oscilator.getBeeman();
        beeman.remove(0);
        for(PosVel pos : beeman){
            writer.write(pos.getPosition() + "\n");
        }
        writer.write("Gear5:\n");
        ArrayList<PosVel> gear5 = oscilator.getGear5();
        gear5.remove(0);
        for(PosVel pos : gear5){
            writer.write(pos.getPosition() + "\n");
        }
        writer.close();

        out = new File("ecm.txt");
        out.createNewFile();
        writer = new FileWriter("ecm.txt", true);

        double ecmV = 0;
        double ecmB = 0;
        double ecmG = 0;
        int i = 0;

        for (Double pos: analytical) {
            ecmV += Math.pow(pos - verlet.get(i).getPosition(), 2);
            ecmB += Math.pow(pos - beeman.get(i).getPosition(), 2);
            ecmG += Math.pow(pos - gear5.get(i).getPosition(), 2);
            i++;
        }

        ecmV = ecmV/analytical.size();
        ecmB = ecmB/analytical.size();
        ecmG = ecmG/analytical.size();

        writer.write("dt: " + Parser.dt + "\n");
        writer.write(ecmV + "\n");
        writer.write(ecmB + "\n");
        writer.write(ecmG + "\n");
        writer.close();

        //Sistema 2
        double L = Parser.D*(Math.sqrt(Parser.N)-1);
        RadiationMatterInteraction rmi = new RadiationMatterInteraction(L, Parser.D, Parser.k2, Parser.N, Parser.M, Parser.Q, Parser.V0max, Parser.V0min, Parser.dt2);

        out = new File("rmi.txt");
        out.createNewFile();
        writer = new FileWriter("rmi.txt");

        ArrayList<Particle> states = rmi.getStates();

        double time = 0.0;
        for (Particle p : states) {
            writer.write(time + ":\n");
            writer.write(p.getPosX() + " " + p.getPosY() + "\n");
            time += Parser.dt;
        }
        writer.close();
    }
}
