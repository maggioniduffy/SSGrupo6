import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.Random;

public class SiloDischarge {

    private static final int MAX_ITERATIONS=50000;
    private double kn, kt, L, W, H, D, dt, rad_prom;
    private int initial_particles;

    private ArrayList<Particle> particles;
    private ArrayList<Double> kinetics;
    private ArrayList<Double> outTimes;

    public int getN() {
        return this.particles.size();
    }
    public SiloDischarge(double kn, double kt, double L, double D, double W, double H, double dt) {
        this.kn = kn;
        this.kt = kt;
        this.L = L;
        this.D = D;
        this.W = W;
        this.H = H;
        this.dt = dt;
        this.rad_prom = 0;
        this.initial_particles = 0;
        this.kinetics = new ArrayList<>();
        this.particles = new ArrayList<>();
        this.outTimes = new ArrayList<>();
        generate_particles();
        getPrevAcc();

    }

    private void generate_particles() {
        int iterations = 0;
        Random randomRad = new Random();
        Random randomX = new Random();
        Random randomY = new Random();
        Random randomZ = new Random();
        double diam;
        double posX;
        double posY;
        double posZ;
        int i = 0;
        while(iterations < MAX_ITERATIONS){
            diam = 0.02 + (0.03 - 0.02) * randomRad.nextDouble();
            posX = diam/2.0 + (this.W - diam) * randomX.nextDouble();
            posY = diam/2.0 + (this.L - diam) * randomY.nextDouble();
            posZ = diam/2.0 + (this.H - diam) * randomZ.nextDouble();
            if(check_positions(posX, posY, posZ, diam/2, -1)){
                this.particles.add(new Particle(i,posX,posY, posZ, posX, posY, posZ, 0.0,0.0, 0.0, diam/2.0, Parser.mass,0.0,-10.0,0.0, 0.0,0.0,0.0));
                i++;
                this.rad_prom += diam/2.0;
            }
            iterations++;
        }
        this.initial_particles = this.particles.size();
        this.rad_prom = this.rad_prom / this.particles.size();
    }
    public void getPrevAcc() {

        for(Particle p : particles) {
            getParticlePrevAcc(p);
        }

    }

    public void getParticlePrevAcc(Particle p) {
        p.setPrevAccX(p.getAccX());
        p.setPrevAccY(p.getAccY());
        p.setPrevAccZ(p.getAccZ());

        getParticleForces(p);
        p.setVelX(p.getVelX() + dt*p.getAccX());
        p.setVelY(p.getVelY() + dt*p.getAccY());
        p.setVelZ(p.getVelZ() + dt*p.getAccZ());
        p.setPosX(p.getPosX() + dt*(p.getVelX() + dt*p.getAccX()));
        p.setPosY(p.getPosY() + dt*(p.getVelY() + dt*p.getAccY()));
        p.setPosZ(p.getPosZ() + dt*(p.getVelZ() + dt*p.getAccZ()));
    }

    public void simulate() throws IOException {
        int iterations = 0;
        ArrayList<Particle> removed = new ArrayList<>();
        double kinetic = 0.0;
        double accX;
        double accY;
        double accZ;
        Date date = new Date();

        File out = new File("output0" + (int)(this.D*100) + ".xyz");
        out.createNewFile();
        FileWriter writer = new FileWriter("output0" + (int)(this.D*100) + ".xyz");
        // writer.write(this.L + " " + this.W + " " + this.D + "\n");
//        writer.write(particles.size() + "\n");
//        writer.write("id xPosition yPosition zPosition xVelocity yVelocity zVelocity radius mass time\n");
        while(iterations <= MAX_ITERATIONS) {
            removed.clear();
            for (Particle p : this.particles) {
                accX = p.getAccX();
                accY = p.getAccY();
                accZ = p.getAccZ();
                kinetic += getKinetic(p);

                getParticleForces(p);
                
                if(p.getPosY() < 0.0 && p.getPrevPosY() >= 0.0) {
                    this.outTimes.add(iterations*this.dt);
                    //System.out.println(outParticles);
                }
                if(!getBeeman(p, accX, accY, accZ)){
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
            if(iterations % 100 == 0){
                // writer.write("iteration\n");
                writer.write(particles.size() + "\n");
                writer.write("id xPosition yPosition zPosition xVelocity yVelocity zVelocity radius mass time\n");
                for(Particle p : this.particles){
                    writer.write(p.getId() + " " + p.getPosX() + " " + p.getPosY() + " " + p.getPosZ() + " " + p.getVelX() + " " + p.getVelY() + " " + p.getVelZ()+ " " + p.getRad() + " " + p.getMass() + " " + this.dt * iterations + "\n");
                }
                print_status(iterations, date);
            }
            kinetic = 0.0;

            //System.out.println(this.particles.size());
            iterations++;
        }
        writer.close();
    }

    private void print_status(int iteration, Date date) throws IOException {
        System.out.print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
        System.out.println("Cantidad de particulas: " + this.initial_particles);
        System.out.println("Progreso: " + iteration*100/MAX_ITERATIONS + "%");
        System.out.println("Tiempo estimado: " + ((MAX_ITERATIONS-iteration)* (new Date().getTime() - date.getTime())/(iteration != 0 ? iteration*1000 : 1))/60 + " minutos");
        // clear terminal
    }

    private boolean reinject_particle(Particle p){
        int iterations = 0;
        Random randomX = new Random();
        Random randomY = new Random();
        Random randomZ = new Random();
        double posX;
        double posY;
        double posZ;
        p.setPrevPosX(p.getPosX());
        p.setPrevPosY(p.getPosY());
        p.setPrevPosZ(p.getPosZ());
        while(iterations < 50000){
            posX = p.getRad() + (this.W - p.getRad()*2) * randomX.nextDouble();
            posY = (p.getRad() + 4*this.L/5) + ((this.L-p.getRad())-(p.getRad()+4*this.L/5)) * randomY.nextDouble();
            posZ = p.getRad() + (this.H - p.getRad()*2) * randomZ.nextDouble();
            p.setPosX(posX);
            p.setPosY(posY);
            p.setPosZ(posZ);
            if(check_positions(posX, posY, posZ, p.getRad(), p.getId())){
                p.setVelY(0.0);
                p.setVelX(0.0);
                p.setVelZ(0.0);
                p.setAccX(0.0);
                p.setAccY(-10.0);
                p.setAccZ(0.0);
                getParticlePrevAcc(p);
                return true;
                //ver si hay que hacer getForces y setear prevAccel
            }

            iterations++;
        }
        return false;
    }

    private boolean check_positions(double posX, double posY, double posZ, double rad, int id){
        for(Particle p : this.particles){
            if(id != p.getId()) {
                double distance = Math.sqrt(Math.pow(posX - p.getPosX(), 2) + Math.pow(posY - p.getPosY(), 2) + Math.pow(posZ - p.getPosZ(), 2));
                if (rad + p.getRad() - distance > 0) {
                    return false;
                }
            }
        }
        return true;
    }

    private double superposition(Particle p1, Particle p2){
        if(p1.getId() != p2.getId()) {
            return p1.getRad() + p2.getRad() - Math.sqrt(Math.pow(p1.getPosX() - p2.getPosX(), 2) + Math.pow(p1.getPosY() - p2.getPosY(), 2) + Math.pow(p1.getPosZ() - p2.getPosZ(), 2));
        }
        return -1;
    }

    private double collision_wall(String wall, Particle p) {
        double result = -1.0;
        if (wall.equals("UP") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(this.L - p.getPosY());
        } else if (wall.equals("DOWN")) {
            if (p.getPosY() < 0) {
                result = -1.0;  // Particle is below the bottom of the silo
            } else {
                double dx = p.getPosX() - this.W / 2.0;
                double dz = p.getPosZ() - this.H / 2.0;
                double distanceFromCenter = Math.sqrt(dx * dx + dz * dz);
                double holeRadius = this.D / 2.0;
                if (distanceFromCenter > holeRadius) {
                    result = p.getRad() - Math.abs(p.getPosY());
                }
            }
        } else if (wall.equals("RIGHT") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(this.W - p.getPosX());
        } else if (wall.equals("LEFT") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(p.getPosX());
        } else if (wall.equals("FRONT") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(this.H - p.getPosZ());
        } else if (wall.equals("BACK") && p.getPosY() > 0) {
            result = p.getRad() - Math.abs(p.getPosZ());
        }
        return result;
    }

    public boolean getBeeman(Particle p, double accX, double accY, double accZ){

        double nextRX = p.getPosX() + p.getVelX() * dt + (2.0/3.0) * accX * Math.pow(dt, 2) - (1.0/6.0) * p.getPrevAccX() * Math.pow(dt, 2);
        double nextRY = p.getPosY() + p.getVelY() * dt + (2.0/3.0) * accY * Math.pow(dt, 2) - (1.0/6.0) * p.getPrevAccY() * Math.pow(dt, 2);
        double nextRZ = p.getPosZ() + p.getVelZ() * dt + (2.0/3.0) * accZ * Math.pow(dt, 2) - (1.0/6.0) * p.getPrevAccZ() * Math.pow(dt, 2);

        double nextVX = p.getVelX() + (1.0/3.0) * p.getAccX() * dt + (5.0/6.0) * accX * dt - (1.0/6.0) * p.getPrevAccX() * dt;
        double nextVY = p.getVelY() + (1.0/3.0) * p.getAccY() * dt + (5.0/6.0) * accY * dt - (1.0/6.0) * p.getPrevAccY() * dt;
        double nextVZ = p.getVelZ() + (1.0/3.0) * p.getAccZ() * dt + (5.0/6.0) * accZ * dt - (1.0/6.0) * p.getPrevAccZ() * dt;

        if(nextRY < -(this.D * 3) ){
            return false;
        }

        p.setPrevPosX(p.getPosX());
        p.setPrevPosY(p.getPosY());
        p.setPrevPosZ(p.getPosZ());
        p.setPosX(nextRX);
        p.setPosY(nextRY);
        p.setPosZ(nextRZ);
       
        p.setPrevVelX(p.getVelX());
        p.setPrevVelY(p.getVelY());
        p.setPrevVelZ(p.getVelZ());
        p.setVelX(nextVX);
        p.setVelY(nextVY);
        p.setVelZ(nextVZ);

        p.setPrevAccX(accX);
        p.setPrevAccY(accY);
        p.setPrevAccZ(accZ);

        return true;
    }

    public void getParticleForces(Particle p) {
        // Inicialización de fuerzas
        double force_x = 0.0;
        double force_y = p.getMass() * -10.0; // Considerando la gravedad
        double force_z = 0.0;
    
        // Interacción entre partículas
        for (Particle p2 : this.particles) {
            if (p != p2) { // Asegura que no comparemos la partícula consigo misma
                double superpos = superposition(p, p2);
                if (superpos > 0) { // Hay superposición, por lo tanto, hay interacción
                    double dx = p2.getPosX() - p.getPosX();
                    double dy = p2.getPosY() - p.getPosY();
                    double dz = p2.getPosZ() - p.getPosZ();
                    double distance = Math.sqrt(dx * dx + dy * dy + dz * dz);
    
                    // Direcciones normalizadas
                    double enx = dx / distance;
                    double eny = dy / distance;
                    double enz = dz / distance;
    
                    // Velocidad relativa
                    double vRelX = p.getVelX() - p2.getVelX();
                    double vRelY = p.getVelY() - p2.getVelY();
                    double vRelZ = p.getVelZ() - p2.getVelZ();

                    double enVrel = enx * vRelX + eny * vRelY + enz * vRelZ;
                    double tangencialVrelX = vRelX - enVrel * enx;
                    double tangencialVrelY = vRelY - enVrel * eny;
                    double tangencialVrelZ = vRelZ - enVrel * enz;
                    
                    // Fuerza normal: proporcional a la superposición
                    double fn = -kn * superpos - Parser.gamma * enVrel;
                    double ft = -kt * superpos;
                    
                    // Fuerza normal
                    force_x += fn * enx;
                    force_y += fn * eny;
                    force_z += fn * enz;

                    // Fuerza tangencial
                    double tangentialVrel = Math.sqrt(tangencialVrelX * tangencialVrelX + tangencialVrelY * tangencialVrelY + tangencialVrelZ * tangencialVrelZ);
                    if (tangentialVrel != 0) {
                        double tx = tangencialVrelX / tangentialVrel;
                        double ty = tangencialVrelY / tangentialVrel;
                        double tz = tangencialVrelZ / tangentialVrel;
                        force_x += ft * tx;
                        force_y += ft * ty;
                        force_z += ft * tz;
                    }
                }
            }
        }
    
        // Interacción con las paredes
        double enx = 0, eny = 0, enz = 0;
        String[] walls = {"UP", "DOWN", "RIGHT", "LEFT", "FRONT", "BACK"};
        for (String wall : walls) {
            double superpos = collision_wall(wall, p);
            if (superpos > 0) {
                switch (wall) {
                    case "UP":
                        eny = 1.0;
                        break;
                    case "DOWN":
                        eny = -1.0;
                        break;
                    case "RIGHT":
                        enx = 1.0;
                        break;
                    case "LEFT":
                        enx = -1.0;
                        break;
                    case "FRONT":
                        enz = 1.0;
                        break;
                    case "BACK":
                        enz = -1.0;
                        break;
                }
                
                double vRelX = p.getVelX();
                double vRelY = p.getVelY();
                double vRelZ = p.getVelZ();
                double enVrel = enx * vRelX + eny * vRelY + enz * vRelZ;
                double tangencialVrelX = vRelX - enVrel * enx;
                double tangencialVrelY = vRelY - enVrel * eny;
                double tangencialVrelZ = vRelZ - enVrel * enz;

                double fn = -kn * superpos - Parser.wallgamma * enVrel;
                double ft = -kt * superpos;

                force_x += fn * enx;
                force_y += fn * eny;
                force_z += fn * enz;

                double tangencialVrel = Math.sqrt(tangencialVrelX * tangencialVrelX + tangencialVrelY * tangencialVrelY + tangencialVrelZ * tangencialVrelZ);
                if (tangencialVrel != 0) {
                    double tx = tangencialVrelX / tangencialVrel;
                    double ty = tangencialVrelY / tangencialVrel;
                    double tz = tangencialVrelZ / tangencialVrel;
                    force_x += ft * tx;
                    force_y += ft * ty;
                    force_z += ft * tz;
                }

            }
        }
    
        // Establecer aceleraciones basadas en las fuerzas acumuladas
        p.setAccX(force_x / p.getMass());
        p.setAccY(force_y / p.getMass());
        p.setAccZ(force_z / p.getMass());
    }
    

    public double getKinetic(Particle particle) {
        return  (particle.getMass()*Math.pow(Math.sqrt(Math.pow(particle.getVelX(),2)+Math.pow(particle.getVelY(),2)+Math.pow(particle.getVelZ(),2)),2))/2;
        // return  (particle.getMass()*Math.pow(Math.sqrt(Math.pow(particle.getVelX(),2)+Math.pow(particle.getVelY(),2)),2))/2;
    }

    public ArrayList<Double> getOutTimes() {
        return this.outTimes;
    }

    public ArrayList<Double> getKinetics() {
        return this.kinetics;
    }

    public double getRad_prom() {return this.rad_prom;}
    public int getInitial_particles() {return this.initial_particles;}
}
