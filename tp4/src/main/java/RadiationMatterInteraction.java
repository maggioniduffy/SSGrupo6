import java.util.ArrayList;
import java.util.Random;

public class RadiationMatterInteraction {

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
    private ArrayList<Particle> states;
    private ArrayList<Double> energies;
    private double e0;


    public RadiationMatterInteraction(double L, double D, double k, double N, double M, double Q, double V0max, double V0min, double dt) {
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
        this.states = new ArrayList<Particle>();
        this.energies = new ArrayList<Double>();

        generateParticles();
        this.e0 = getEnergy();
        Double[] f = getCoulombForce();
        prevR[0] = particle.getPosX() - dt * particle.getVelX() + (Math.pow(dt,2)/(2*M))*f[0];
        prevR[1] = particle.getPosY() - dt * particle.getVelY() + (Math.pow(dt,2)/(2*M))*f[1];
        saveStates(0,false);
        simulate();
    }

    public Double[] getCoulombForce() {
        double fx = 0;
        double fy = 0;
        for (FixedParticle p : this.particles) {
            double rx = particle.getPosX() - p.getPosX();
            double ry = particle.getPosY() - p.getPosY();
            double module = Math.sqrt(Math.pow(rx,2) + Math.pow(ry,2));
            double faux = p.getQ()/Math.pow(module,2);

            fx += faux * rx/module;
            fy += faux * ry/module;
        }

        fx = fx*k*particle.getQ();
        fy = fy*k*particle.getQ();
        Double[] f = {fx,fy};
        return f;
    }

    public double getKinetic() {
        return  (particle.getMass()*Math.pow(Math.sqrt(Math.pow(particle.getVelX(),2)+Math.pow(particle.getVelY(),2)),2))/2;
    }

    public double getPotential() {
        double u = 0;
        double posp = Math.sqrt(Math.pow(particle.getPosX(),2)+Math.pow(particle.getPosY(),2));
        for (FixedParticle p : this.particles) {
            double posaux = Math.sqrt(Math.pow(p.getPosX(),2)+Math.pow(p.getPosY(),2));
            u += p.getQ()/Math.abs(posp-posaux);
        }

        u = u*k*particle.getQ();
        return u;
    }

    public double getEnergy() {
        return getKinetic() + getPotential();
    }

    public void generateParticles() {
        int s = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= N; j++) {
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
        int it = 0;
        while(particle.getPosX()<=(L+D) && particle.getPosX()>=0 && particle.getPosY()>=0 && particle.getPosY()<=L && distanceToFixedParticle() && it<1000000){
            Double[] f = getCoulombForce();
            updateParticle(f);
            saveStates(it,false);
            it++;
        }
        if(it % 50 != 0) {
            saveStates(it, true);
        }
    }

    public boolean distanceToFixedParticle() {
        for (FixedParticle p : particles) {
            double distance = Math.sqrt(Math.pow(p.getPosX() - particle.getPosX(), 2) +
                    Math.pow(p.getPosY() - particle.getPosY(), 2));

            if (distance < 0.01 * D){
                System.out.println("Absorbed");
                return false;
            }
        }
        return true;
    }

    private void saveStates(int it, boolean last_iter) {
        Particle p = new Particle(particle.getPosX(), particle.getPosY(), particle.getVelX(), particle.getVelY(), M, Q);
        if(it % 50 == 0 || last_iter) { //guardo cada 50 iteraciones
            states.add(p);
            double e = e0 - getEnergy();
            if (e < 0) {
                e = e * (-1);
            }
            energies.add(e);
        }
    }

    double[] prevR ={0,0};
    private void updateParticle(Double[] f) {
        double rx = 2*particle.getPosX() - prevR[0] + (Math.pow(dt,2)/M) * f[0] ;
        double ry = 2*particle.getPosY() - prevR[1] + (Math.pow(dt,2)/M) * f[1] ;

        prevR[0] = particle.getPosX();
        prevR[1] = particle.getPosY();

        particle.setPosX(rx);
        particle.setPosY(ry);

        particle.setVelX((rx - prevR[0])/(2*dt));
        particle.setVelY((ry - prevR[1])/(2*dt));
    }

    public ArrayList<Particle> getStates() {
        return states;
    }
}
