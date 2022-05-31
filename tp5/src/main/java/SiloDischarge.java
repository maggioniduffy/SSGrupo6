import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class SiloDischarge {
    private double kn, kt, L, W, D, dt;

    private ArrayList<Particle> particles;
    private ArrayList<Double> kinetics;
    private ArrayList<Integer> outParticlesArr;

    public int getN() {
        return this.particles.size();
    }
    public SiloDischarge(double kn, double L, double W, double D, double dt) {
        this.kn = kn;
        this.kt = 2*kn;
        this.L = L;
        this.W = W;
        this.D = D;
        this.dt = dt;
        this.kinetics = new ArrayList<>();
        this.particles = new ArrayList<>();
        this.outParticlesArr = new ArrayList<>();
        generate_particles();
    }

    private void generate_particles() {
        int iterations = 0;
        Random randomRad = new Random();
        Random randomX = new Random();
        Random randomY = new Random();
        double diam;
        double posX;
        double posY;
        int i = 0;
        while(iterations < 50000){
            diam = 0.02 + (0.03 - 0.02) * randomRad.nextDouble();
            posX = diam/2.0 + (this.W - diam) * randomX.nextDouble();
            posY = diam/2.0 + (this.L - diam) * randomY.nextDouble();
            if(check_positions(posX, posY, diam/2, -1)){
                this.particles.add(new Particle(i,posX,posY, posY,0.0,0.0, diam/2.0, Parser.mass,0.0,-10.0, 0.0,0.0));
                i++;
            }
            iterations++;
        }
    }

    public void simulate() throws IOException {
        int iterations = 0;
        ArrayList<Particle> removed = new ArrayList<>();
        double kinetic = 0.0;
        double accX;
        double accY;
        int outParticles = 0;
        File out = new File("output.txt");
        out.createNewFile();
        FileWriter writer = new FileWriter("output.txt");
        writer.write(this.L + " " + this.W + " " + this.D + "\n");
        while(iterations <= 500000) {
            removed.clear();
            for (Particle p : this.particles) {
                accX = p.getAccX();
                accY = p.getAccY();
                kinetic += getKinetic(p);

                getParticleForces(p);

                if(p.getPosY() < 0.0 && p.getPrevPosY() >= 0.0) {
                    outParticles++;
                    //System.out.println(outParticles);
                }
                if(!getBeeman(p, accX, accY)){
                    if(!reinject_particle(p)){
                        removed.add(p);
                    }
                }
            }
            if(removed.size() > 0){
                System.out.println(removed);
            }
            this.particles.removeAll(removed);
            this.kinetics.add(kinetic);

//                System.out.println(iterations);
            if(iterations % 1000 == 0){
                this.outParticlesArr.add(outParticles);
                outParticles = 0;
                writer.write("iteration\n");
                for(Particle p : this.particles){
                    writer.write(p.getRad() + " " + p.getPosX() + " " + p.getPosY() + "\n");
                }
            }
            kinetic = 0.0;

            //System.out.println(this.particles.size());
            iterations++;
        }
        writer.close();
    }

    private boolean reinject_particle(Particle p){
        int iterations = 0;
        Random randomX = new Random();
        Random randomY = new Random();
        double posX;
        double posY;
        while(iterations < 50000){
            posX = p.getRad() + (this.W - p.getRad()*2) * randomX.nextDouble();
            posY = (p.getRad() + 4*this.L/5) + ((this.L-p.getRad())-(p.getRad()+4*this.L/5)) * randomY.nextDouble();
            p.setPrevPosY(p.getPosY());
            p.setPosX(posX);
            p.setPosY(posY);
            if(check_positions(posX, posY, p.getRad(), p.getId())){
                p.setVelY(0.0);
                p.setVelX(0.0);
                p.setAccX(0.0);
                p.setAccY(-10.0);
                return true;
                //ver si hay que hacer getForces y setear prevAccel
            }

            iterations++;
        }
        return false;
    }

    private boolean check_positions(double posX, double posY, double rad, int id){
        for(Particle p : this.particles){
            if(id != p.getId()) {
                double distance = Math.sqrt(Math.pow(posX - p.getPosX(), 2) + Math.pow(posY - p.getPosY(), 2));
                if (rad + p.getRad() - distance > 0) {
                    return false;
                }
            }
        }
        return true;
    }

    private double superposition(Particle p1, Particle p2){
        if(p1.getId() != p2.getId()) {
            return p1.getRad() + p2.getRad() - Math.sqrt(Math.pow(p1.getPosX() - p2.getPosX(), 2) + Math.pow(p1.getPosY() - p2.getPosY(), 2));
        }
        return -1;
    }

    private double collision_wall(String wall, Particle p){
        double result = -1.0;
        if(wall.equals("UP") && p.getPosY() > 0){
            result = p.getRad() - Math.abs(this.L - p.getPosY());
        } else if (wall.equals("DOWN")) {
            if((p.getPosX() > this.W/2.0 - this.D/2.0 && p.getPosX() < this.W/2.0 + this.D/2.0) || p.getPosY() < 0)
                result = -1.0;
            else
                result = p.getRad() - Math.abs(p.getPosY());
        } else if (wall.equals("RIGHT") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(this.W - p.getPosX());
        } else if (wall.equals("LEFT") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(p.getPosX());
        }
        return result;
    }

    public boolean getBeeman(Particle p, double accX, double accY){

        double nextRX = p.getPosX() + p.getVelX() * dt + (2.0/3.0) * accX * Math.pow(dt, 2) - (1.0/6.0) * p.getPrevAccX() * Math.pow(dt, 2);
        double nextRY = p.getPosY() + p.getVelY() * dt + (2.0/3.0) * accY * Math.pow(dt, 2) - (1.0/6.0) * p.getPrevAccY() * Math.pow(dt, 2);

        double nextVX = p.getVelX() + (1.0/3.0) * p.getAccX() * dt + (5.0/6.0) * accX * dt - (1.0/6.0) * p.getPrevAccX() * dt;
        double nextVY = p.getVelY() + (1.0/3.0) * p.getAccY() * dt + (5.0/6.0) * accY * dt - (1.0/6.0) * p.getPrevAccY() * dt;

        if(nextRY < -L/10){
            return false;
        }

        p.setPrevPosY(p.getPosY());
        p.setPosX(nextRX);
        p.setPosY(nextRY);

        p.setVelX(nextVX);
        p.setVelY(nextVY);

        p.setPrevAccX(accX);
        p.setPrevAccY(accY);

        return true;
    }

    public void getParticleForces(Particle p){
        double force_y = p.getMass() * -10.0;
        double force_x = 0.0;
        String walls[] = {"UP", "DOWN", "RIGHT", "LEFT"};
        double enx = 0.0;
        double eny = 0.0;
        for(Particle p2 : this.particles){

            double superpos = superposition(p, p2);
            if(superpos >= 0){
                double distance_x = p2.getPosX() - p.getPosX();
                double distance_y = p2.getPosY() - p.getPosY();
                double distance = Math.sqrt(Math.pow(distance_x, 2) + Math.pow(distance_y, 2));

                enx = distance_x/distance;
                eny = distance_y/distance;

                double fn = -kn*superpos;
                double ft = -kt*superpos*((p.getVelX() - p2.getVelX())*(-eny) + (p.getVelY() - p2.getVelY())*enx);

                force_x = force_x + fn*enx - ft*eny;
                force_y = force_y + fn*eny + ft*enx;
            }

        }

        for(String wall : walls){
            double superpos = collision_wall(wall, p);
            if(superpos >= 0){
                if(wall.equals("UP")){
                    enx = 0.0;
                    eny = 1.0;
                } else if (wall.equals("DOWN")) {
                    enx = 0.0;
                    eny = -1.0;
                } else if (wall.equals("RIGHT")) {
                    enx = 1.0;
                    eny = 0.0;
                } else {
                    enx = -1.0;
                    eny = 0.0;
                }

                double fn = -kn*superpos;
                double ft = -kt*superpos*(-p.getVelX()*eny + p.getVelY()*enx);

                force_x = force_x + fn*enx - ft*eny;
                force_y = force_y + fn*eny + ft*enx;
            }
        }

        p.setAccX(force_x/p.getMass());
        p.setAccY(force_y/p.getMass());


    }

    public double getKinetic(Particle particle) {
        return  (particle.getMass()*Math.pow(Math.sqrt(Math.pow(particle.getVelX(),2)+Math.pow(particle.getVelY(),2)),2))/2;
    }

    public ArrayList<Integer> getOutParticles() {
        return this.outParticlesArr;
    }

    public ArrayList<Double> getKinetics() {
        return this.kinetics;
    }

}
