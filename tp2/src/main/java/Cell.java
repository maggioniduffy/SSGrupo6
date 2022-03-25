public class Cell {
    private boolean alive;
    private int column;
    private int row;
    private int id;

    public Cell(boolean alive, int col, int row, int id){
        this.alive = alive;
        this.column = col;
        this.row = row;
        this.id = id;
    }

    public boolean isAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
