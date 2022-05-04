public class Beeman {
    private double mass;
    private double dt;
    private double k;
    private double gamma;

    public Beeman(double mass, double dt, double k, double gamma) {
        this.mass = mass;
        this.dt = dt;
        this.k = k;
        this.gamma = gamma;
    }

    public PosVel getBeeman(double currentR, double currentV, double currentForce, double prevForce){
        double nextR = currentR + currentV * dt + (2/3) * (currentForce/mass) * Math.pow(dt, 2) - (1/6) * (prevForce/mass) * Math.pow(dt, 2);
        double predV = currentV + (3/2) * (currentForce / mass) * dt - (1/2) * (prevForce / mass) * dt;
        double nextF = - this.k * nextR - this.gamma * predV;
        double corrV = currentV + (1/3) * (nextF / mass) * dt + (5/6) * (currentForce/mass) * dt - (1/6) * (prevForce/mass) * dt;

        return new PosVel(nextR, corrV);
    }
}
