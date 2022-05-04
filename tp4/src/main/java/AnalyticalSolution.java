public class AnalyticalSolution {
    private double mass;
    private double k;
    private double gamma;

    public AnalyticalSolution(double mass, double k, double gamma){
        this.mass = mass;
        this.k = k;
        this.gamma = gamma;
    }

    public double getAnalyticalSolution(double time){
        double exp = Math.exp(-(this.gamma / (2 * this.mass)) * time);
        double cos = Math.cos(Math.pow(((this.k / this.mass) - (Math.pow(this.gamma, 2) / (4 * Math.pow(this.mass, 2)))), 0.5) * time);
        return exp * cos;
    }

}
