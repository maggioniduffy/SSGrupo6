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
    float time;

    public Collision(float time, CollisionType collisionType, Particle p1){
        this.type = collisionType;
        this.p1 = p1;
        this.time = time;
    }
    public Collision(float time, CollisionType collisionType, Particle p1, Particle p2){
        this.type = collisionType;
        this.p1 = p1;
        this.p2 = p2;
        this.time = time;
    }
}