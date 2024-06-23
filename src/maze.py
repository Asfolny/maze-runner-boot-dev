from cell import Cell
from point import Point
import time

class Maze:
    """A maze builder
    start_point is a Point of x,y; this is the top_left of the maze itself
    cell_size is also a point, for convenience of having .x and .y
    master is the above laying Window class this all happens under, since the maze is made up out of Cell instances, master MUST implement draw_line()"""
    def __init__(
        self,
        start_point,
        num_rows,
        num_cols,
        cell_size,
        master=None
    ):
        self._cells = []
        self._start_point = start_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._master = master

        self._create_cells()

    def _create_cells(self):
        # Nothing here really prevents us from generating cells outside the master's view
        for col in range(self._num_cols):
            col_cells = []

            for row in range(self._num_rows):
                col_cells.append(Cell(self._master))
            
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self._master is None:
            return

        x1 = self._start_point.x + i * self._cell_size.x
        y1 = self._start_point.y + j * self._cell_size.y
        x2 = x1 + self._cell_size.x
        y2 = y1 + self._cell_size.y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self._master is None:
            return

        self._master.redraw()
        time.sleep(.2)
