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

    public void updatePosition(float time) {
        this.posX = this.posX + (this.velX * time); //Habria que usar la velocidad inicial en vez de this.posX en el primer termino?
        this.posY = this.posY + (this.velY * time); //Igual que con X
    }

    public float timeToParticleCollision(Particle particle){

        double deltaR[] = {this.posX - particle.getPosX(), this.posY - particle.getPosY()};
        double deltaV[] = {this.velX - particle.getVelX(), this.velY - particle.getVelY()};
        double deltas = deltaV[0] * deltaR[0] + deltaV[1] * deltaR[1];
        if (deltas >= 0){
            return Float.MAX_VALUE;
        }
        double sigma = this.rad + particle.getRad();
        float escDeltaV = (float) (Math.pow(deltaV[0], 2) + Math.pow(deltaV[1], 2));
        float escDeltaR = (float) (Math.pow(deltaR[0], 2) + Math.pow(deltaR[1], 2));

        float d = (float) (Math.pow(deltas, 2) - escDeltaV * ( escDeltaR - Math.pow(sigma, 2)));
        if (d < 0){
            return Float.MAX_VALUE;
        }
        float collisionTime = (float) -((deltas + Math.sqrt(d)) / escDeltaV);

        return  collisionTime;
    }

    public float timeToVerticalWallCollision(float size){
        float collisionTime;
        float collisionTimeXver = Float.MAX_VALUE;

        if (this.velX > 0.0f){
            collisionTimeXver =  (float) ((size - this.rad - this.posX) / this.velX);
        } else if (this.velX < 0.0f) {
            collisionTimeXver = (float) ((this.rad - this.posX) / this.velX);
        }

        collisionTime = collisionTimeXver ;
        return collisionTime;
    }

    public Float timeToHorizontalWallCollision(float size){
        Float collisionTime;
        Float collisionTimeYhor=Float.MAX_VALUE;

        if (this.velY > 0.0f){
            collisionTimeYhor =  (float) ((size - this.rad - this.posY) / this.velY);
        } else if (this.velY < 0.0f){
            collisionTimeYhor = (float) ((this.rad - this.posY) / this.velY);
        }
        collisionTime = collisionTimeYhor;

        return collisionTime;
    }
}
