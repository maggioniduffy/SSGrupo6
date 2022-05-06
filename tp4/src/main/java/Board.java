import java.util.ArrayList;
import java.util.Random;

public class Board {

    private double L;
    private double D;
    private double k;
    private double N;
    private double M;
    private double Q;
    private double V0max;
    private double V0min;
    private double dt;
    private ArrayList<FixedParticle> particles;
    private Particle particle;


    public Board(double L, double D, double k, double N, double M, double Q, double V0max, double V0min, double dt) {
        this.L = L;
        this.D = D;
        this.k = k;
        this.N = N;
        this.M = M;
        this.Q = Q;
        this.V0max = V0max;
        this.V0min = V0min;
        this.dt = dt;
        this.particles = new ArrayList<FixedParticle>();
        generateParticles();
    }

    public double getForce() {
        double f = k*particle.getQ();
        double posp = Math.sqrt(Math.pow(particle.getPosX(),2)+Math.pow(particle.getPosY(),2));
        for (FixedParticle p : this.particles) {
            double posaux = Math.sqrt(Math.pow(p.getPosX(),2)+Math.pow(p.getPosY(),2));
            f += p.getQ()/Math.pow(posp-posaux,2)*((posp*posaux)/Math.abs(posp*posaux));
        }
        return f;
    }

    public double getKinetic() {
        return  (particle.getMass()*Math.pow(Math.sqrt(Math.pow(particle.getVelX(),2)+Math.pow(particle.getVelY(),2)),2))/2;
    }

    public double getPotential() {
        double u = k*particle.getQ();
        double posp = Math.sqrt(Math.pow(particle.getPosX(),2)+Math.pow(particle.getPosY(),2));
        for (FixedParticle p : this.particles) {
            double posaux = Math.sqrt(Math.pow(p.getPosX(),2)+Math.pow(p.getPosY(),2));
            u += p.getQ()/Math.abs(posp-posaux);
        }
        return u;
    }

    public double getEnergy() {
        return getKinetic() + getPotential();
    }

    public void generateParticles() {
        int s = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < N; j++) {
                this.particles.add(new FixedParticle(D * j, D * i, M, s * Q));
                s = s * (-1);
            }
            s = s * (-1);
        }

        Random r = new Random();
        Random r2 = new Random();
        particle = new Particle(0,((L/2)-D) + r.nextFloat() * (((L/2)+D) - ((L/2)-D)), V0min + r2.nextFloat() * (V0max - V0min),0, M, Q);
    }

    public void simulate() {
        double t = 0;
        while(particle.getPosX()<L+D && particle.getPosX()>0 && particle.getPosY()>0 && particle.getPosY()<L){

        }
    }
}
