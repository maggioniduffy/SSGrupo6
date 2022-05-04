public class PosVel {
    private double position;
    private double velocity;

    public PosVel(double position, double velocity) {
        this.position = position;
        this.velocity = velocity;
    }

    public double getPosition() {
        return position;
    }

    public void setPosition(double position) {
        this.position = position;
    }

    public double getVelocity() {
        return velocity;
    }

    public void setVelocity(double velocity) {
        this.velocity = velocity;
    }
}
