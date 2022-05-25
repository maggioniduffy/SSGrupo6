import com.sun.xml.internal.ws.wsdl.writer.document.Part;

import java.util.ArrayList;
import java.util.Random;

public class SiloDischarge {
    private double kn, kt, L, W, D, dt;


    private ArrayList<Particle> particles;

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
        this.particles = new ArrayList<>();
        generate_particles();
    }

    private void generate_particles(){
        int iterations = 0;
        Random randomRad = new Random();
        Random randomX = new Random();
        Random randomY = new Random();
        double diam;
        double posX;
        double posY;
        while(iterations < 50000){
            diam = 0.02 + (0.03 - 0.02) * randomRad.nextDouble();
            posX = this.W * randomX.nextDouble();
            posY = this.L * randomY.nextDouble();
            if(check_positions(posX, posY, diam/2)){
                this.particles.add(new Particle(posX,posY,0,0, diam/2, Parser.mass,0,-10.0, 0,0));
            }
            iterations++;
        }
    }

    private boolean check_positions(double posX, double posY, double rad){
        for(Particle p : this.particles){
            double distance = Math.sqrt(Math.pow(posX - p.getPosX(), 2) + Math.pow(posY - p.getPosY(), 2));
            if(rad + p.getRad() - distance > 0){
                return false;
            }
        }
        return true;
    }


}
