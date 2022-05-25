public class Beeman {
    private double mass;
    private double dt;

    public Beeman(double mass, double dt, double k, double gamma) {
        this.mass = mass;
        this.dt = dt;
    }

    public boolean getBeeman(Particle p, double accX, double accY){

        double nextRX = p.getPosX() + p.getVelX() * dt + (2.0/3) * accX * Math.pow(dt, 2) - (1.0/6) * p.getPrevAccX() * Math.pow(dt, 2);
        double nextRY = p.getPosY() + p.getVelY() * dt + (2.0/3) * accY * Math.pow(dt, 2) - (1.0/6) * p.getPrevAccY() * Math.pow(dt, 2);

        double nextVX = p.getVelX() + (1.0/3) * p.getAccX() * dt + (5.0/6) * accX * dt - (1.0/6) * p.getPrevAccX() * dt;
        double nextVY = p.getVelY() + (1.0/3) * p.getAccY() * dt + (5.0/6) * accY * dt - (1.0/6) * p.getPrevAccY() * dt;

        p.setPosX(nextRX);
        p.setPosY(nextRY);

        p.setVelX(nextVX);
        p.setVelY(nextVY);

        p.setPrevAccX(accX);
        p.setPrevAccY(accY);

        return true;
    }
}
