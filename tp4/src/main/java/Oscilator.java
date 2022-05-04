import java.util.ArrayList;

public class Oscilator {

    private double mass;
    private double k;
    private double gamma;
    private double tf;
    private double r0;
    private double dt;
    private AnalyticalSolution as;
    private Verlet ver;
    private Beeman bee;
    private Gear5 g5;
    ArrayList<Double> analytical = new ArrayList<>();
    ArrayList<PosVel> verlet = new ArrayList<>();
    ArrayList<PosVel> beeman = new ArrayList<>();
    ArrayList<PosVel> gear5 = new ArrayList<>();

    public Oscilator(double mass, double k, double gamma, double tf, double r0, double dt) {
        this.mass = mass;
        this.k = k;
        this.gamma = gamma;
        this.tf = tf;
        this.r0 = r0;
        this.dt = dt;
        this.as = new AnalyticalSolution(mass, k, gamma);
        this.ver = new Verlet(mass, dt);
        this.bee = new Beeman(mass, dt, k, gamma);
        this.g5 = new Gear5(gamma, mass, k, dt);

        double v0 = (-r0) * (gamma / (2 * mass));
        this.analytical.add(r0);

        PosVel euler = new PosVel(r0 - dt * v0 + Math.pow(dt, 2) * getForce(r0, v0) / (2 * mass), v0 - (dt / mass) * getForce(r0, v0));
        PosVel posvel0 = new PosVel(r0, v0);
        this.verlet.add(euler);
        this.verlet.add(posvel0);
        this.gear5.add(euler);
        this.gear5.add(posvel0);
        this.beeman.add(euler);
        this.beeman.add(posvel0);

    }

    public void solution() {
        double t = dt;
        while(t < this.tf){
            PosVel currVerlet = this.verlet.get(this.verlet.size()-1);
            PosVel prevVerlet = this.verlet.get(this.verlet.size()-2);
            PosVel currBeeman = this.beeman.get(this.beeman.size()-1);
            PosVel prevBeeman = this.beeman.get(this.beeman.size()-2);
            PosVel currGear5 = this.beeman.get(this.gear5.size()-1);
            this.analytical.add(this.as.getAnalyticalSolution(t));
            this.verlet.add(this.ver.getVerlet(getForce(currVerlet.getPosition(), currVerlet.getVelocity()), currVerlet.getPosition(), prevVerlet.getPosition()));
            this.beeman.add(this.bee.getBeeman(currBeeman.getPosition(),currBeeman.getVelocity(),getForce(currBeeman.getPosition(),currBeeman.getVelocity()),getForce(prevBeeman.getPosition(),prevBeeman.getVelocity())));
            this.gear5.add(this.g5.getGear5(getForce(currGear5.getPosition(), currGear5.getVelocity()), currGear5.getVelocity(), currGear5.getPosition()));
            t += dt;
        }
    }

    public ArrayList<Double> getAnalytical() {
        return analytical;
    }

    public ArrayList<PosVel> getVerlet() {
        return verlet;
    }

    public ArrayList<PosVel> getBeeman() {
        return beeman;
    }

    public ArrayList<PosVel> getGear5() {
        return gear5;
    }

    private double getForce(double r, double v) {
        return - this.k * r - this.gamma * v;
    }
}
