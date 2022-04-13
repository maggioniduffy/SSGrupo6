// No se si hace falta esto:
enum CollisionType {
    VERTICALWALL,
    HORIZONTALWALL,
    PARTICLE
}

class Collision{

    CollisionType type;
    Particle p1;
    Particle p2;
    double time;

    public Collision(double time, CollisionType type, Particle p1){
        this.type = type;
        this.p1 = p1;
        this.time = time;
    }
    public Collision(double time, CollisionType type, Particle p1, Particle p2){
        this.type = type;
        this.p1 = p1;
        this.p2 = p2;
        this.time = time;
    }
}