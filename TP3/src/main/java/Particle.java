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

    public double getCollTime() {
        return collTime;
    }

    public void setCollTime(double collTime) {
        this.collTime = collTime;
    }

    public void updatePosition(double collTime) {
        this.posX = this.posX + (this.velX * collTime); //Habria que usar la velocidad inicial en vez de this.posX en el primer termino?
        this.posY = this.posY + (this.velY * collTime); //Igual que con X
    }

    public double timeToParticleCollision(Particle particle){

        double deltaPosX = this.posX - particle.getPosX();
        double deltaPosY = this.posY - particle.getPosY();
        double deltaVelX = this.velX - particle.getVelX();
        double deltaVelY = this.velY - particle.getVelY();
        double deltas = deltaPosX * deltaVelX + deltaPosY * deltaVelY;

        if (deltas >= 0){
            return Double.MAX_VALUE;
        }

        double sigma = this.rad + particle.getRad();
        double escDeltaR = (Math.pow(deltaPosX, 2) + Math.pow(deltaPosY, 2));
        double escDeltaV = (Math.pow(deltaVelX, 2) + Math.pow(deltaVelY, 2));

        double d = (Math.pow(deltas, 2) - escDeltaV * ( escDeltaR - Math.pow(sigma, 2)));
        if (d < 0){
            return Double.MAX_VALUE;
        }
        double collTime = - ((deltas + Math.sqrt(d)) / escDeltaV);

        return  collTime;
    }

    public double timeToVerticalWallCollision(double size){

        double collTime = Double.MAX_VALUE;

        if (this.velX > 0.0){
            collTime = ((size - this.rad - this.posX) / this.velX);
        } else if (this.velX < 0.0) {
            collTime = ((this.rad - this.posX) / this.velX);
        }

        return collTime;
    }

    public double timeToHorizontalWallCollision(double size){

        double collTime = Double.MAX_VALUE;

        if (this.velY > 0.0){
            collTime = ((size - this.rad - this.posY) / this.velY);
        } else if (this.velY < 0.0){
            collTime = ((this.rad - this.posY) / this.velY);
        }

        return collTime;
    }
}
