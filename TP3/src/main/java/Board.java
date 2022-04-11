import java.util.*;
import static java.lang.Math.*;

public class Board {
    static int SIDE_SIZE = 6;
    static int MIN_PARTICLES = 100;
    static int MAX_PARTICLES = 150;
    static double SMALL_RADIUS = 0.2;
    static double SMALL_MASS = 0.9;
    static double BIG_RADIUS = 0.7;
    static double BIG_MASS = 2;
    private static int MAX_ITERATIONS = 20000;
    private static int MAX_ATTEMPS = 20000;

    private double maxVelocity;
    private double bigParticleX = 0;
    private double bigParticleY = 0;
    private double center = SIDE_SIZE/2;

    private List<Particle> particles = new ArrayList<Particle>();
    public SortedMap<Float, List<Particle>> states = new TreeMap<>();
    float time = 0;

    int iterations = 0;

    public Board(double maxVelocity) {
        this.maxVelocity = maxVelocity;
        createParticles();
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

            double x = (random.nextDouble() * (SMALL_RADIUS*2) - SMALL_RADIUS);
            double y = (random.nextDouble() * (SMALL_RADIUS*2) - SMALL_RADIUS);

            if (appendParticle(x, y, SMALL_RADIUS, SMALL_MASS)) {
                particlesNumber += 1;
            }
            attempt += 1;
        }
    }

    private boolean appendParticle(double xPos, double yPos, double radius, double mass) {
        for (Particle p : particles) {

            float distance = (float) (sqrt((yPos - p.getPosY()) * (yPos - p.getPosY()) + (xPos - p.getPosX()) * (xPos - p.getPosX())) - (p.getRad() + SMALL_RADIUS));
            if (distance < 0)
                return false;
        }
        Random r = new Random();
        float velocity = (float) (maxVelocity * r.nextDouble());
        float angle = (float) Math.toRadians(Math.random() * 360);

        float xVel = (float) (velocity * Math.cos(angle));
        float yVel = (float) (velocity * Math.sin(angle));

        particles.add(new Particle(xPos, yPos, xVel, yVel, SMALL_RADIUS, SMALL_MASS));

        return true;
    }
}
