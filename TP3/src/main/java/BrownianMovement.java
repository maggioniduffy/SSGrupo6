import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.SortedMap;
import java.util.TreeMap;
import java.math.BigDecimal;
public class BrownianMovement {
    private static int MAX_ITERATIONS = 80000;
    private static double MAX_SIMULATED_TIME = 200000;
    private double time = 0;
    private int iterations = 0;
    private Board board;
    private ArrayList<Particle> particles;
    public SortedMap<Double, List<Particle>> states = new TreeMap<>();
    private List<Collision> colls;
    private FileWriter writer;
    private FileWriter speedWriter;
    private int collisionNumber = 0;

    public BrownianMovement(Board board, FileWriter writer, FileWriter speedWriter){
        this.board = board;
        this.particles = board.getParticles();
        this.writer = writer;
        this.speedWriter = speedWriter;
    }

    public void start() throws IOException {
        List<Particle> clone = (List<Particle>) this.particles.clone();
        //states.put(time, clone);
        this.firstOutput();
        while(!stop()){
            double next = getNextCollisionTime();
            collisionNumber++;
            updateStatus(next);
            updateSpeeds();
            iterations ++;
        }
    }

    private boolean stop(){

        boolean res = false;
        double x = this.particles.get(0).getPosX();
        double y =  this.particles.get(0).getPosY();

        double aux = board.SIDE_SIZE - board.BIG_RADIUS;
        if( x <= board.BIG_RADIUS || y<= board.BIG_RADIUS || y >= aux || x >= aux){
            System.out.println("flag " + iterations);
            res = true;
        }
        //System.out.println(res || (this.iterations >= MAX_ITERATIONS)  || (this.time >= MAX_SIMULATED_TIME));
        return res || (this.iterations >= MAX_ITERATIONS)  || (this.time >= MAX_SIMULATED_TIME) ;
    }

    private double getNextCollisionTime(){

        double nextEventTime = Double.MAX_VALUE;
        colls = new ArrayList<>();

        for (int i = 0; i < particles.size(); i++){
            double verticalCollTime = particles.get(i).timeToVerticalWallCollision(board.SIDE_SIZE);
            double horizontalCollTime = particles.get(i).timeToHorizontalWallCollision(board.SIDE_SIZE);
            double particleCollTime = Double.MAX_VALUE;

            int selectedJ = 0;

            for (int j = i + 1; j < particles.size(); j++){
                double particleTime = particles.get(i).timeToParticleCollision(particles.get(j));

                if (particleTime < particleCollTime){
                    particleCollTime = particleTime;
                    selectedJ = j;
                }
            }

            double eventTime = Math.min(Math.min(horizontalCollTime, verticalCollTime), particleCollTime);

            if (eventTime <= nextEventTime){

                if (eventTime < nextEventTime){
                    colls.clear(); // ESTO POR QUE?
                }

                nextEventTime = eventTime;

                if ((eventTime == verticalCollTime) && eventTime != Double.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.VERTICALWALL, particles.get(i)));
                }
                if ((eventTime == horizontalCollTime) && eventTime != Double.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.HORIZONTALWALL, particles.get(i)));
                }
                if ((eventTime == particleCollTime) && eventTime != Double.MAX_VALUE) {
                    colls.add(new Collision(eventTime, CollisionType.PARTICLE, particles.get(i), particles.get(selectedJ)));
                }
            }
        }

        return nextEventTime;
    }
    int s = 1;
    private void updateStatus(double collTime) throws IOException {
        if (s == 1) {
            System.out.println(collTime);
        }
        time += collTime;
        if (s == 1) {
            System.out.println(time);
        }
        double aux_time = (double)Math.round(time * 1000000d) / 1000000d;
        if (s == 1) {
            System.out.println(aux_time);
        }
        this.s++;
        //System.out.println(aux_time);
        writer.write("Collision");
        writer.write("\n");
        writer.write("Time " + aux_time);
        writer.write("\n");

        speedWriter.write("Collision");
        speedWriter.write("\n");
        speedWriter.write("Time " + aux_time);
        speedWriter.write("\n");
        this.writeParticles(collTime);
    }

    private void writeParticles(double collTime) throws IOException {
        int i = 0;
        for (Particle p : particles){
            p.updatePosition(collTime);
            writer.write(i + ":" + p.getPosX() + "," + p.getPosY());
            writer.write("\n");
            double aux_x_speed  = (double)Math.round(Math.abs(p.getVelX()) * 1000000d) / 1000000d;
            double aux_y_speed = (double)Math.round(Math.abs(p.getVelY()) * 1000000d) / 1000000d;
            double speed = Math.sqrt(aux_x_speed*aux_x_speed + aux_y_speed*aux_y_speed);
            speed = (double)Math.round(speed * 1000000d) / 1000000d;
            speedWriter.write(i + ":" + speed);
            speedWriter.write("\n");
            i++;
        }
    }

    private void firstOutput() throws IOException {
        writer.write("Collision");
        writer.write("\n");
        writer.write("Time 0");
        writer.write("\n");

        speedWriter.write("Collision");
        speedWriter.write("\n");
        speedWriter.write("Time 0");
        speedWriter.write("\n");
        int i = 0;
        for (Particle p : particles) {
            writer.write(i + ":" + p.getPosX() + "," + p.getPosY());
            writer.write("\n");
            double aux_x_speed  = (double)Math.round(Math.abs(p.getVelX()) * 1000000d) / 1000000d;
            double aux_y_speed = (double)Math.round(Math.abs(p.getVelY()) * 1000000d) / 1000000d;
            double speed = Math.sqrt(aux_x_speed*aux_x_speed + aux_y_speed*aux_y_speed);
            speed = (double)Math.round(speed * 1000000d) / 1000000d;
            speedWriter.write(i + ":" + speed);
            speedWriter.write("\n");
            i++;
        }
    }



    private void updateSpeeds(){

        for (Collision c : colls){
            if (c.type == CollisionType.VERTICALWALL){
                double xVel = c.p1.getVelX() * -1;
                c.p1.setVelX(xVel);
            } else if (c.type == CollisionType.HORIZONTALWALL){
                double yVel = c.p1.getVelY() * -1;
                c.p1.setVelY(yVel);
            } else {

                double deltaPosX = c.p1.getPosX() - c.p2.getPosX();
                double deltaPosY = c.p1.getPosY() - c.p2.getPosY();
                double deltaVelX = c.p1.getVelX() - c.p2.getVelX();
                double deltaVelY = c.p1.getVelY() - c.p2.getVelY();
                double deltas = deltaPosX * deltaVelX + deltaPosY * deltaVelY;

                double sigma = c.p1.getRad() + c.p2.getRad();

                double m1 = c.p1.getMass();
                double m2 = c.p2.getMass();

                double j = (2 * m1 * m2 * deltas) / (sigma * (m1 + m2));
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