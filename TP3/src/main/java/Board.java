import java.util.*;

public class Board {
    final int SIDE_SIZE = 6;
    final int MIN_PARTICLES = 100;
    final int MAX_PARTICLES = 150;
    final double SMALL_RADIUS = 0.2;
    final double SMALL_MASS = 0.9;
    final double BIG_RADIUS = 0.7;
    final double BIG_MASS = 2;
    private static int MAX_ATTEMPS = 2000;

    private double maxVelocity;
    private double bigParticleX = 0;
    private double bigParticleY = 0;
    private double center = SIDE_SIZE/2;

    private ArrayList<Particle> particles = new ArrayList<Particle>();
    
    public Board(double maxVelocity) {
        this.maxVelocity = maxVelocity;
        this.createParticles();
    }

    public ArrayList<Particle> getParticles() {
        return particles;
    }

    private void createParticles() {
        particles.add(
                new Particle(
                center,
                center,
                bigParticleX,
                bigParticleY,
                BIG_RADIUS,
                BIG_MASS));

        int particlesNumber = 1;
        int attempt = 0;

        Random random = new Random();
        int quantity = random.nextInt(MAX_PARTICLES-MIN_PARTICLES) + MIN_PARTICLES;

        while (particlesNumber != quantity && attempt != MAX_ATTEMPS) {

            double aux = SIDE_SIZE-SMALL_RADIUS;
            double x = (SMALL_RADIUS + (aux - SMALL_RADIUS) * random.nextDouble());
            double y = (SMALL_RADIUS + (aux - SMALL_RADIUS) * random.nextDouble());
            if (appendParticle(x, y)) {
                particlesNumber += 1;
            }
            attempt += 1;
        }
    }

    private boolean appendParticle(double xPos, double yPos) {
        for (Particle p : particles) {
            double distance = (Math.sqrt((yPos - p.getPosY()) * (yPos - p.getPosY()) + (xPos - p.getPosX()) * (xPos - p.getPosX())) - (p.getRad() + SMALL_RADIUS));
            if (distance < 0)
                return false;
        }
        Random r = new Random();
        double velocity = (maxVelocity * r.nextDouble());
        double angle = Math.toRadians(Math.random() * 360);

        double xVel = (velocity * Math.cos(angle));
        double yVel = (velocity * Math.sin(angle));

        particles.add(new Particle(xPos, yPos, xVel, yVel, SMALL_RADIUS, SMALL_MASS));

        return true;
    }
}
