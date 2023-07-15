public class Particle implements Comparable<Particle>{

    private double posX, posY, posZ, prevPosX, prevPosY, prevPosZ, velX, velY, velZ, prevVelX, prevVelY, prevVelZ, rad, mass, accX, accY, accZ, prevAccX, prevAccY, prevAccZ;
    private int id;
    public Particle(int id, double posX, double posY, double posZ, double prevPosX, double prevPosY, double prevPosZ, double velX, double velY, double velZ, double rad, double mass, double accX, double accY, double accZ,  double prevAccX, double prevAccY, double prevAccZ) 
    {
        this.id = id;
        this.posX = posX;
        this.posY = posY;
        this.posZ = posZ;
        this.prevPosX = prevPosX;
        this.prevPosY = prevPosY;
        this.prevPosZ = prevPosZ;
        this.velX = velX;
        this.velY = velY;
        this.velZ = velZ;
        this.rad = rad;
        this.mass = mass;
        this.accX = accX;
        this.accY = accY;
        this.accZ = accZ;
        this.prevAccX = prevAccX;
        this.prevAccY = prevAccY;
        this.prevAccZ = prevAccZ;
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

    public double getPosZ() {
        return posZ;
    }

    public void setPosZ(double posZ) {
        this.posZ = posZ;
    }

    public double getPrevPosX() {
        return prevPosX;
    }

    public void setPrevPosX(double prevPosX) {
        this.prevPosX = prevPosX;
    }

    public double getPrevPosY() {
        return prevPosY;
    }

    public void setPrevPosY(double prevPosY) {
        this.prevPosY = prevPosY;
    }

    public double getPrevPosZ() {
        return prevPosZ;
    }

    public void setPrevPosZ(double prevPosZ) {
        this.prevPosZ = prevPosZ;
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

    public double getVelZ() {
        return velZ;
    }

    public void setVelZ(double velZ) {
        this.velZ = velZ;
    }

    public double getPrevVelX() {
        return prevVelX;
    }

    public void setPrevVelX(double prevVelX) {
        this.prevVelX = prevVelX;
    }

    public double getPrevVelY() {
        return prevVelY;
    }

    public void setPrevVelY(double prevVelY) {
        this.prevVelY = prevVelY;
    }

    public double getPrevVelZ() {
        return prevVelZ;
    }

    public void setPrevVelZ(double prevVelZ) {
        this.prevVelZ = prevVelZ;
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

    public double getAccZ() {
        return accZ;
    }

    public void setAccZ(double accZ) {
        this.accZ = accZ;
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

    public double getPrevAccZ() {
        return prevAccZ;
    }

    public void setPrevAccZ(double prevAccZ) {
        this.prevAccZ = prevAccZ;
    }



    @Override
    public int compareTo(Particle particle) {
        if(id==particle.id)
            return 0;
        return -1;
    }
}