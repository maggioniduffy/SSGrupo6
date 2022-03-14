import java.util.Set;
import java.util.TreeSet;

public class Cell {

    private double x;
    private double y;
    private Set<Particle> particles;

    public Cell(double x, double y) {
        this.x = x;
        this.y = y;
        this.particles = new TreeSet<Particle>();
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public Set<Particle> getParticles() {
        return particles;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void addParticle(Particle particle){
        this.particles.add(particle);
    }
}
