public class Main {
    public static void main(String[] args) {
        Board board = new Board(2);
        BrownianMovement bm = new BrownianMovement(board);
        bm.start();
    }
}
