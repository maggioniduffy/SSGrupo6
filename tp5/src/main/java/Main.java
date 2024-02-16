import org.json.simple.parser.ParseException;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws IOException, ParseException, InterruptedException {
        Parser.parse();

        double[] diams = {0.40, 0.60};
        int totalIterations = diams.length;

        // Crea un ExecutorService con tantos hilos como núcleos disponibles en el procesador
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        for (int i = 0; i < diams.length; i++) {
            final int iteration = i + 1;
            final double diam = diams[i];

            // Envía una tarea al ExecutorService para ejecutarla en un hilo separado
            executor.submit(() -> {
                try {
                    SiloDischarge silo = new SiloDischarge(Parser.kn, diam * Parser.kn, Parser.L, 0.18, Parser.W, Parser.H, Parser.dt, iteration, totalIterations);
                    silo.simulate();

                    saveResults(silo, diam);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
        }

        // Espera a que todas las tareas se completen y cierra el ExecutorService
        executor.shutdown();
        executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
    }

    private static void saveResults(SiloDischarge silo, double diam) throws IOException {
        File out = new File("caudal0" + (int) (diam * 100) + ".txt");
        out.createNewFile();
        FileWriter writer = new FileWriter(out);
        writer.write(silo.getInitial_particles() + " " + silo.getRad_prom() + "\n");
        writer.write("D:" + diam + "\n");
        for (Double outTime : silo.getOutTimes()) {
            writer.write(outTime + "\n");
        }
        writer.close();

        ArrayList<Double> kinetics = silo.getKinetics();
        out = new File("kinetic0" + (int) (diam * 100) + ".txt");
        out.createNewFile();
        writer = new FileWriter(out);
        writer.write("D:" + diam + "\n");
        for (Double kinetic : kinetics) {
            writer.write(kinetic + "\n");
        }
        writer.close();
    }
}
