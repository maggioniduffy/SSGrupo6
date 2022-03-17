package ar.edu.itba.ss;
import java.io.FileNotFoundException;
import java.io.IOException;

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
			
			for (Particle p : Parser.particles){
	            System.out.print(p.getId());
	            for (Particle neighbour : p.getNeighbours()){
	                System.out.print(" " + neighbour.getId());
	            }
	            System.out.print("\n");
	        }
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
