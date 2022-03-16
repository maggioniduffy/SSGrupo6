package ar.edu.itba.ss;
import java.util.Set;
import java.util.TreeSet;

public class Particle implements Comparable<Particle>{

    private Integer id;
    private double x;
    private double y;
    private double r;
    private Set<Particle> neighbours;
    private Cell cell;

    public Particle(Integer id, double r) {
        this.id = id;
        this.r = r;
        this.neighbours = new TreeSet<Particle>();
    }

    public Integer getId() {
        return id;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getR() {
        return r;
    }
    
    public Cell getCell() {
    	return cell;
    }

    public Set<Particle> getNeighbours() {
        return neighbours;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setR(double r) {
        this.r = r;
    }
    
    public void setCell(Cell cell) {
        this.cell = cell;
    }

    public void addNeighbour(Particle neighbour){
        this.neighbours.add(neighbour);
    }

    public double distanceTo(Particle particle){
        return Math.sqrt(Math.pow(x - particle.getX(), 2) +
                Math.pow(y - particle.getY(), 2))
                - r - particle.getR();
    }
    
    public double periodicDistanceTo(Particle particle){

        double dx = Math.abs(this.x - particle.x);
        if (dx > Parser.L / 2)
            dx = Parser.L - dx;

        double dy = Math.abs(this.y - particle.y);
        if (dy > Parser.L / 2)
            dy = Parser.L - dy;

        return Math.sqrt(Math.pow(dx,2) + Math.pow(dy,2));
    }

    public int compareTo(Particle particle){
        return id - particle.getId();
    }

    @Override
    public int hashCode() {
        return this.id.hashCode();
    }
}
