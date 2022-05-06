public class FixedParticle {

    private double posX, posY, mass, q;

    public FixedParticle(double posX, double posY, double mass, double q) {
        this.posX = posX;
        this.posY = posY;
        this.mass = mass;
        this.q = q;
    }

    public double getPosX() {
        return posX;
    }

    public void setPosX(double posX) {
        this.posX = posX;
    }

    public double getPosY() {
        return posY;
    }

    public void setPosY(double posY) {
        this.posY = posY;
    }

    public double getMass() {
        return mass;
    }

    public void setMass(double mass) {
        this.mass = mass;
    }

    public double getQ() {
        return q;
    }

    public void setQ(double q) {
        this.q = q;
    }
}
