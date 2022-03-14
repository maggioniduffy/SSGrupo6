import java.util.Set;
import java.util.TreeSet;

public class Particle implements Comparable<Particle>{

    private Integer id;
    private double x;
    private double y;
    private double r;
    private Set<Particle> neighbours;

    public Particle(Integer id, double x, double y, double r) {
        this.id = id;
        this.x = x;
        this.y = y;
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

    public void addNeighbour(Particle neighbour){
        this.neighbours.add(neighbour);
    }

    public double getDistanceTo(Particle particle){
        return Math.sqrt(Math.pow(x - particle.getX(), 2) +
                Math.pow(y - particle.getY(), 2))
                - r - particle.getR();
    }

    public int compareTo(Particle particle){
        return id - particle.getId();
    }

    @Override
    public int hashCode() {
        return this.id.hashCode();
    }
}
