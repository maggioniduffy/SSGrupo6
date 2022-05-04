public class Verlet {
    private double mass;
    private double dt;

    public Verlet(double mass, double dt) {
        this.mass = mass;
        this.dt = dt;
    }

    public PosVel getVerlet(double force, double currentR, double prevR){
        double nextR = 2 * currentR - prevR + Math.pow(dt, 2) * force / mass;
        double nextV = (nextR - prevR) / (2*dt);

        return new PosVel(nextR, nextV);
    }
}
