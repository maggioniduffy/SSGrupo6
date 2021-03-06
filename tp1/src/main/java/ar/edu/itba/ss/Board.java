package ar.edu.itba.ss;
import java.util.ArrayList;
import java.util.Set;

import static ar.edu.itba.ss.Parser.particles;
import static ar.edu.itba.ss.Parser.periodicContour;
public class Board {

    private ArrayList<Cell> cells;
    private double L;
    private int M;
    private int N;
    private double rc;

    public Board(double L, int M, int N, double rc) {
        this.L = L;
        this.M = M;
        this.N = N;
        this.rc = rc;
        this.cells = new ArrayList<Cell>();
        createCells();
    }

    private void createCells() {
        Integer n = 0;
        for(int i = 0 ; i < this.M ; i++) {
            for(int j = 0 ; j < this.M  ; j++) {
                System.out.println("celula: " + n + " x: "+ i + "y: " + j);
                this.cells.add(new Cell(n, i, j));
                n++;
            }
        }
    }

    public ArrayList<Cell> getCells() {
        return cells;
    }

    public double getSideSize() {
        return L;
    }

    public int getCellsPerLine() {
        return M;
    }

    public int getNumberOfParticles() {
        return N;
    }

    public double getRc() {
        return rc;
    }
    
    public void bruteForce(){
        for (Particle p1: particles){
            for (Particle p2: particles){
                if (!p1.equals(p2) && !p1.getNeighbours().contains(p2)){

                    double distance;

                    if (periodicContour){
                        distance = p1.periodicDistanceTo(p2);
                    }else{
                        distance = p1.distanceTo(p2);
                    }

                    if (distance < Parser.rc){
                        p1.addNeighbour(p2);
                        p2.addNeighbour(p1);
                    }
                }
            }
        }
    }
    
    public void cellIndexMethod(){
        int cellX = 0;
        int cellY = 0;

        for (Particle p : particles){
            System.out.println("Particle: " + p.getId());
            System.out.println("X: " + p.getX() + " Y: " + p.getY());
            cellX = (int) Math.floor(p.getX() / (this.L/this.M));
            System.out.println("cellX: " + cellX);
            cellY = (int) Math.floor(p.getY() / (this.L/this.M));
            System.out.println("cellY: " + cellY);
            int cellNumber = (int) (cellY * this.M + cellX);
            System.out.println("Cellnumber: " + cellNumber);
            Cell cell = cells.get(cellNumber);
            p.setCell(cell);
            p.setCellX(cellX);
            p.setCellY(cellY);
            cell.addParticle(p);
        }

        for (Cell c : cells){
            System.out.println("c" + c.getId());
            for (Particle p : c.getParticles()){
            	checkNeighbourCells(p, p.getCellX(), p.getCellY());
                checkNeighbourCells(p, p.getCellX(), p.getCellY() + 1);
                checkNeighbourCells(p, p.getCellX() + 1, p.getCellY() + 1);
                checkNeighbourCells(p, p.getCellX() + 1, p.getCellY());
                checkNeighbourCells(p, p.getCellX() + 1, p.getCellY() - 1);
            }
        }

    }

    private void checkNeighbourCells(Particle particle, int cellX, int cellY) {

        if (periodicContour) {

            if (cellX >= this.M ){
                cellX = 0;
            }

            if (cellY >= this.M ){
                cellY = 0;
            }

            if (cellX == -1){
                cellX = this.M - 1;
            }

            if (cellY == -1){
                cellY = this.M - 1;
            }

        }else {
            System.out.println("cellX: " + cellX + "M: " + this.M);
            if (cellX >= this.M  || cellX < 0 || cellY >= this.M || cellY < 0) {
                System.out.println("PARTICULA NUMERO: " + particle.getId() + " SALIO ");
                return;
            }
        }

        int neighbourCellNumber = (int) (cellY * this.M  + cellX);
        System.out.println("Particle: " + particle + ", neighbor cell X: " + cellX + ", " + cellY + "cell index: " + neighbourCellNumber);
        Set<Particle> cellParticles = cells.get(neighbourCellNumber).getParticles();

        for (Particle neighbourParticle : cellParticles){

            if (neighbourParticle.getId() != particle.getId()){

                double distance;

                if (periodicContour){
                    distance = particle.periodicDistanceTo(neighbourParticle);
                }else{
                    distance = particle.distanceTo(neighbourParticle);
                }

                if (distance < Parser.rc){
                    particle.addNeighbour(neighbourParticle);
                    neighbourParticle.addNeighbour(particle);
                }

            }
        }
    }


}
