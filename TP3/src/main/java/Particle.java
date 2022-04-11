public class Particle {
    private double posX, posY, velX, velY, rad, mass, collTime;

    public Particle(double posX, double posY, double velX, double velY, double rad, double mass) {
        this.posX = posX;
        this.posY = posY;
        this.velX = velX;
        this.velY = velY;
        this.rad = rad;
        this.mass = mass;
    }

    public double getPosX() {
        return posX;
    }

    public void setPosX(float posX) {
        this.posX = posX;
    }

    public double getPosY() {
        return posY;
    }

    public void setPosY(float posY) {
        this.posY = posY;
    }

    public double getVelX() {
        return velX;
    }

    public void setVelX(float velX) {
        this.velX = velX;
    }

    public double getVelY() {
        return velY;
    }

    public void setVelY(float velY) {
        this.velY = velY;
    }

    public double getRad() {
        return rad;
    }

    public void setRad(float rad) {
        this.rad = rad;
    }

    public double getMass() {
        return mass;
    }

    public void setMass(float mass) {
        this.mass = mass;
    }

    public double getCollTime() {
        return collTime;
    }

    public void setCollTime(float collTime) {
        this.collTime = collTime;
    }
}
