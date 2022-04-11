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
        List<Particle> copy = (List<Particle>) this.particles.clone();
        states.put(time, copy);

        while(!finish()) {
            float next = getNextCollisionTime();
            updateStatus(next);
            generateCollision();

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

            float verticalCollisionTime = particles.get(i).verticalWallCollision(board.SIDE_SIZE);
            float horizontalCollisionTime = particles.get(i).horizontalWallCollision(board.SIDE_SIZE));
            float particleCollisionTime = Float.MAX_VALUE;

            int selectedJ = 0;

            for (int j = i + 1; j < particles.size(); j++) {

                float particleTime = particles.get(i).particleCollision(particles.get(j));

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


}
