public class Gear5 {
    double gamma;
    double mass;
    double k;
    double dt;

    public Gear5(double gamma, double mass, double k, double dt) {
        this.gamma = gamma;
        this.mass = mass;
        this.k = k;
        this.dt = dt;
    }

    public PosVel getGear5(double currentForce, double currentV, double currentR){
        
        double r2 = currentForce / this.mass;
        double r3 = - this.k * currentV / this.mass - this.gamma * r2 / this.mass;
        double r4 = - this.k * r2 / this.mass - this.gamma * r3 / this.mass;
        double r5 = - this.k * r3 / this.mass - this.gamma * r4 / this.mass;
        double rP = currentR + currentV * this.dt + r2 * Math.pow(this.dt, 2) / 2 + r3 * Math.pow(this.dt, 3) / 6 + r4 * Math.pow(this.dt, 4) / 24 + r5 * Math.pow(this.dt, 5) / 120;
        double r1P = currentV + r2 * this.dt + r3 * Math.pow(this.dt, 2) / 2 + r4 * Math.pow(this.dt, 3) / 6 + r5 * Math.pow(this.dt, 4) / 24;
        double r2P = r2 + r3 * this.dt + r4 * Math.pow(this.dt, 2) / 2 + r5 * Math.pow(this.dt, 3) / 6;
        double r3P = r3 + r4 * this.dt + r5 * Math.pow(this.dt, 2) / 2;
        double r4P = r4 + r5 * this.dt;
        double r5P = r5;
        double deltaR2 = ((- this.k * rP - this.gamma * r1P) / this.mass - r2P) * (float) Math.pow(this.dt, 2) / 2;
        double nextR = rP + deltaR2 * 3 / 16;
        double nextV = r1P + (251 * deltaR2) / (360 + this.dt);

        return new PosVel(nextR, nextV);
    }
}
