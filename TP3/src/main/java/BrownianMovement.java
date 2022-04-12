import java.util.ArrayList;
import java.util.List;
import java.util.SortedMap;
import java.util.TreeMap;

public class BrownianMovement {
    private static int MAX_ITERATIONS = 20000;
    private static float MAX_SIMULATED_TIME = 20000;
    private float time = 0;
    private int iterations = 0;
    private Board board;
    private ArrayList<Particle> particles;
    public SortedMap<Float, List<Particle>> states = new TreeMap<>();
    private List<Collision> colls;

    public BrownianMovement(Board board) {
        this.board = board;
        this.particles = board.getParticles();
    }

    public void start(){
        List<Particle> clone = (List<Particle>) this.particles.clone();
        states.put(time, clone);

        while(!finish()) {
            float next = getNextCollisionTime();
            updateStatus(next);
            updateSpeeds();
            iterations +=1;
        }
    }


    private boolean finish(){
        boolean res = false;
        double x = this.particles.get(0).getPosX();
        double y =  this.particles.get(0).getPosY();


        double aux = board.SIDE_SIZE - board.SMALL_RADIUS;
        if( x<= board.BIG_RADIUS || y<= board.BIG_RADIUS || y >= aux || x >= aux){
            System.out.println("flag " + iterations);
            res = true;
        }

        return res && (iterations < MAX_ITERATIONS)  && (time < MAX_SIMULATED_TIME) ;
    }

    private float getNextCollisionTime() {
        float nextEventTime = Float.MAX_VALUE;
        colls = new ArrayList<>();

        for (int i = 0; i < particles.size(); i++) {

            float verticalCollisionTime = particles.get(i).timeToVerticalWallCollision(board.SIDE_SIZE);
            float horizontalCollisionTime = particles.get(i).timeToHorizontalWallCollision(board.SIDE_SIZE);
            float particleCollisionTime = Float.MAX_VALUE;

            int selectedJ = 0;

            for (int j = i + 1; j < particles.size(); j++) {

                float particleTime = particles.get(i).timeToParticleCollision(particles.get(j));

                if (particleTime < particleCollisionTime) {
                    particleCollisionTime = particleTime;
                    selectedJ = j;
                }
            }

            float eventTime = Math.min(Math.min(horizontalCollisionTime, verticalCollisionTime), particleCollisionTime);

            if (eventTime <= nextEventTime) {

                if (eventTime < nextEventTime) {
                    colls.clear(); // ESTO POR QUE?
                }

                nextEventTime = eventTime;

                if ((eventTime == verticalCollisionTime) && eventTime != Float.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.VERTICALWALL, particles.get(i)));
                }
                if ((eventTime == horizontalCollisionTime) && eventTime != Float.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.HORIZONTALWALL, particles.get(i)));
                }
                if ((eventTime == particleCollisionTime) && eventTime != Float.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.PARTICLE, particles.get(i), particles.get(selectedJ)));
                }
            }
        }

        return nextEventTime;
    }

    private void updateStatus(float collisionTime) {
        for (Particle p : particles) {
            p.updatePosition(collisionTime);
        }
        time += collisionTime;
        List<Particle> clone = (List<Particle>) this.particles.clone();;
        states.put(time, clone);
    }

    private void updateSpeeds(){
        for (Collision c : colls){
            if (c.type == CollisionType.VERTICALWALL) {
                double xVel = c.p1.getVelX() * -1;
                c.p1.setVelX(xVel);
            } else if (c.type == CollisionType.HORIZONTALWALL) {
                double yVel = c.p1.getVelY() * -1;
                c.p1.setVelY(yVel);
            } else {

                double deltaX = c.p1.getPosX() - c.p2.getPosX();
                double deltaY = c.p1.getPosY() - c.p2.getPosY();
                double deltaR[] = {deltaX, deltaY};

                double deltaVX = c.p1.getVelX() - c.p2.getVelX();
                double deltaVY = c.p1.getVelY() - c.p2.getVelY();
                double deltaV[] = {deltaVX, deltaVY};
                double esc = deltaV[0] * deltaR[0] + deltaV[1] * deltaR[1]; //deltaV.deltaR

                double sigma = c.p1.getRad() + c.p2.getRad();

                double m1 = c.p1.getMass();
                double m2 = c.p2.getMass();

                double j = (2 * m1 * m2 * esc) / (sigma * (m1 + m2));
                double jX = (j * (c.p1.getPosX() - c.p2.getPosX())) / sigma;
                double jY = (j * (c.p1.getPosY() - c.p2.getPosY())) / sigma;

                double velP1x = c.p1.getVelX() - (jX / m1);
                double velP1y = c.p1.getVelY() - (jY / m1);

                c.p1.setVelX(velP1x);
                c.p1.setVelY(velP1y);

                double velP2x = c.p2.getVelX() + (jX / m2);
                double velP2y = c.p2.getVelY() + (jY / m2);

                c.p2.setVelX(velP2x);
                c.p2.setVelY(velP2y);
            }
        }
    }
}