public class Particle implements Comparable<Particle>{

    private double posX, posY, velX, velY, rad, mass, accX, accY, prevAccX, prevAccY;
    private int id;
    public Particle(int id, double posX, double posY, double velX, double velY, double rad, double mass, double accX, double accY, double prevAccX, double prevAccY) {
        this.id = id;
        this.posX = posX;
        this.posY = posY;
        this.velX = velX;
        this.velY = velY;
        this.rad = rad;
        this.mass = mass;
        this.accX = accX;
        this.accY = accY;
        this.prevAccX = prevAccX;
        this.prevAccY = prevAccY;
    }

    public int getId() {return id;}
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

    public double getVelX() {
        return velX;
    }

    public void setVelX(double velX) {
        this.velX = velX;
    }

    public double getVelY() {
        return velY;
    }

    public void setVelY(double velY) {
        this.velY = velY;
    }

    public double getRad() {
        return rad;
    }

    public void setRad(double rad) {
        this.rad = rad;
    }

    public double getMass() {
        return mass;
    }

    public void setMass(double mass) {
        this.mass = mass;
    }

    public double getAccX() {
        return accX;
    }

    public void setAccX(double accX) {
        this.accX = accX;
    }

    public double getAccY() {
        return accY;
    }

    public void setAccY(double accY) {
        this.accY = accY;
    }

    public double getPrevAccX() {
        return prevAccX;
    }

    public void setPrevAccX(double prevAccX) {
        this.prevAccX = prevAccX;
    }

    public double getPrevAccY() {
        return prevAccY;
    }

    public void setPrevAccY(double prevAccY) {
        this.prevAccY = prevAccY;
    }


    @Override
    public int compareTo(Particle particle) {
        if(id==particle.id)
            return 0;
        return -1;
    }
}