from cell import Cell
from point import Point
import time
import random

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
        master=None,
        seed=None
    ):
        self._cells = []
        self._start_point = start_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._master = master

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

        # Reset visited to re-use it for traversal from in to exit
        for cell_col in self._cells:
            for cell in cell_col:
                cell.visited = False

    def _create_cells(self):
        # Nothing here really prevents us from generating cells outside the master's view
        for col in range(self._num_cols):
            col_cells = []

            for row in range(self._num_rows):
                col_cells.append(Cell(master=self._master))
            
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
         
    def _break_entrance_and_exit(self):
        self._cells[0][0].walls["N"] = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].walls["S"] = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            # east
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # west
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # north
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # south
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here, just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # east
            if next_index[0] == i + 1:
                self._cells[i][j].walls["E"] = False
                self._cells[i + 1][j].walls["W"] = False
            # west
            if next_index[0] == i - 1:
                self._cells[i][j].walls["W"] = False
                self._cells[i - 1][j].walls["E"] = False
            # south
            if next_index[1] == j + 1:
                self._cells[i][j].walls["S"] = False
                self._cells[i][j + 1].walls["N"] = False
            # north
            if next_index[1] == j - 1:
                self._cells[i][j].walls["N"] = False
                self._cells[i][j - 1].walls["S"] = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _animate(self):
        if self._master is None:
            return

        self._master.redraw()
        time.sleep(.2)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # No east wall and non-visited cell? Move
        if (
            i > 0
            and not self._cells[i][j].walls["W"]
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # No east wall and non-visited cell? Move
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].walls["E"]
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # No north wall and non-visited cell? Move
        if (
            j > 0
            and not self._cells[i][j].walls["N"]
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # No south wall and non-visited cell? Move
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].walls["S"]
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # Wrong way
        return False

