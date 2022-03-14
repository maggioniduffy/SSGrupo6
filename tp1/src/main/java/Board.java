public class Board {

    private Cell[] cells;
    private double sideSize;
    private int cellsPerLine;
    private int numberOfParticles;
    private double rc;

    public Board(double sideSize, int cellsPerLine, int numberOfParticles, double rc) {
        this.sideSize = sideSize;
        this.cellsPerLine = cellsPerLine;
        this.numberOfParticles = numberOfParticles;
        this.rc = rc;
        this.cells = new Cell[cellsPerLine * cellsPerLine];
        createCells();
    }

    private void createCells() {
        int n = 1;
        for(int i = 0 ; i < this.cellsPerLine ; i++) {
            for(int j = 0 ; j < this.cellsPerLine  ; j++) {
                this.cells[n] = new Cell(i * this.sideSize/this.cellsPerLine, j * this.sideSize/this.cellsPerLine);
                n++;
            }
        }
    }

    public Cell[] getCells() {
        return cells;
    }

    public double getSideSize() {
        return sideSize;
    }

    public int getCellsPerLine() {
        return cellsPerLine;
    }

    public int getNumberOfParticles() {
        return numberOfParticles;
    }

    public double getRc() {
        return rc;
    }

}
