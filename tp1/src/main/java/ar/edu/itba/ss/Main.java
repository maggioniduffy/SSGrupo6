package ar.edu.itba.ss;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import org.json.simple.parser.ParseException;
import ar.edu.itba.ss.Parser;

public class Main {
	public static void main(String[] args) {
		try {
			Parser.parse();
			Board board = new Board(Parser.L, Parser.M, Parser.N, Parser.rc);
			long start = System.currentTimeMillis();
			if(Parser.method == 1) {
				board.bruteForce();
			} else {
				board.cellIndexMethod();
			}
			long stop = System.currentTimeMillis();
			long time = stop - start;
			System.out.println("Elapsed time: " + time + "ms");
			File out = new File("output.txt");
			out.createNewFile();
			FileWriter writer = new FileWriter("output.txt");
			for (Particle p : Parser.particles){
	            writer.write(p.getId().toString());
	            for (Particle neighbour : p.getNeighbours()){
	                writer.write("," + neighbour.getId().toString());
	            }
	            writer.write("\n");
	        }
			writer.close();

			/*
			ProcessBuilder processBuilder = new ProcessBuilder("python", resolvePythonScriptPath("hello.py"));
			processBuilder.redirectErrorStream(true);

			Process process = processBuilder.start();
			List<String> results = readProcessOutput(process.getInputStream());

			assertThat("Results should not be empty", results, is(not(empty())));
			assertThat("Results should contain output of script: ", results, hasItem(
					containsString("Hello Baeldung Readers!!")));

			int exitCode = process.waitFor();
			assertEquals("No errors should be detected", 0, exitCode);

			 */
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
