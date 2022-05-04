import org.json.simple.parser.ParseException;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws IOException, ParseException {
        Parser.parse();
        File out = new File("output.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("output.txt");
        Oscilator oscilator = new Oscilator(Parser.mass, Parser.k, Parser.gamma, Parser.tf, Parser.r0, Parser.dt);
        oscilator.solution();
        writer.write("Analytical:\n");
        for(Double pos : oscilator.getAnalytical()){
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
    }
}
