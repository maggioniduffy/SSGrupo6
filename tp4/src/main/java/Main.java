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

        System.out.println("Starting System 2");
        //Sistema 2
        double L = Parser.D*(Parser.N-1);
        RadiationMatterInteraction rmi = new RadiationMatterInteraction(L, Parser.D, Parser.k2, Parser.N, Parser.M, Parser.Q, Parser.V0max, Parser.V0min, Parser.dt2);

        out = new File("rmi.txt");
        out.createNewFile();
        writer = new FileWriter("rmi.txt");

        ArrayList<Particle> states = rmi.getStates();

        double longt = 0.0;
        //dts: 1e-15, 1e-16, 1e-17
        double time = 0.0;
        for (int j = 0; j < states.size(); j++) {
            writer.write("t\n");
            writer.write(time + ":\n");
            writer.write(states.get(j).getPosX() + " " + states.get(j).getPosY() + "\n");
            time += Parser.dt2;
            if(j > 0) {
                longt += Math.abs(Math.sqrt(Math.pow(states.get(j).getPosX(),2)+Math.pow(states.get(j).getPosY(),2)) - Math.sqrt(Math.pow(states.get(j-1).getPosX(),2)+Math.pow(states.get(j-1).getPosY(),2)));
            }
        }
        writer.close();

        //V0s: 5000, 16250, 27500, 38750, 50000
//        out = new File("longT50000.txt");
//        out.createNewFile();
//        writer = new FileWriter("longT50000.txt", true);
//
//        writer.write("V0: 50000" + "\n");
//        writer.write(longt + "\n");
//
//        writer.close();

//        out = new File("energies1e-18.txt");
//        out.createNewFile();
//        writer = new FileWriter("energies1e-18.txt", true);
//
//        ArrayList<Double> energies = rmi.getEnergies();
//        writer.write("dt: " + Parser.dt2 + "\n");
//        for (Double e : energies) {
//            writer.write(e + "\n");
//        }
//        writer.close();
    }
}
