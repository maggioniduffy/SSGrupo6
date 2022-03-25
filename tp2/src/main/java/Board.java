import java.util.ArrayList;

public class Board {
    private int numberOfLines;
    private int cellsPerLine;
    private ArrayList<Cell> cells;

    public Board(int lines, int cellsPerLine) {
        this.numberOfLines = lines;
        this.cellsPerLine = cellsPerLine;
        this.cells = new ArrayList<Cell>();
    }

    public void fillCells() {
        int pos = 0;
        for (int i=0; i < numberOfLines; i++) {
            for (int j=0; j < cellsPerLine; j++) {
                boolean alive = Math.random() < 0.5;
                Cell newCell = new Cell(alive, j, i, pos);
                pos++;
                cells.add(newCell);
            }
        }
    }

    public ArrayList<Cell> getNextState() {
        ArrayList<Cell> cellsClone = (ArrayList<Cell>) this.cells.clone();
        for (Cell c: cellsClone) {
            int aliveNeighbors = 0;
            int id = c.getId();
            int newId = id+1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id-1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id - this.cellsPerLine;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id + this.cellsPerLine;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id - this.cellsPerLine + 1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id - this.cellsPerLine - 1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id + this.cellsPerLine + 1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            newId = id + this.cellsPerLine - 1;
            if (!(newId < 0 || newId >= cellsPerLine * numberOfLines)) {
                if (cells.get(newId).isAlive()) {
                    aliveNeighbors++;
                }
            }

            boolean isAlive = c.isAlive();
            if (isAlive && !(aliveNeighbors == 2 || aliveNeighbors == 3)) {
                c.setAlive(false);
            }

            if (!isAlive && aliveNeighbors == 3) {
                c.setAlive(true);
            }
        }

        this.cells = cellsClone;
        return cellsClone;
    }

}
