from line import Line
from point import Point

class Cell:
    """A single cell within the maze
    Taking in a Point instance for top_left coordinates
    Another point for bottom_right coordinates
    A master element as it's drawing place, note that master must have a 'draw_line' function
    And a walls tuple of N, E, S, W"""

    def __init__(self, top_left=None, bottom_right=None, master=None, walls=(True, True, True, True)):
        self.walls = walls
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._master = master
        
    def _draw(self):
        if self._master is None or self._top_left is None or self._bottom_right is None:
            return

        if self.walls[0]:
            self._master.draw_line(
                Line(
                    Point(self._top_left.x, self._top_left.y),
                    Point(self._bottom_right.x, self._top_left.y)
                ),
                "green"
            )

        if self.walls[1]:
            self._master.draw_line(
                Line(
                    Point(self._bottom_right.x, self._top_left.y),
                    Point(self._bottom_right.x, self._bottom_right.y)
                ),
                "green"
            )

        if self.walls[2]:
            self._master.draw_line(
                Line(
                    Point(self._top_left.x, self._bottom_right.y),
                    Point(self._bottom_right.x, self._bottom_right.y)
                ),
                "green"
            )

        if self.walls[3]:
            self._master.draw_line(
                Line(
                    Point(self._top_left.x, self._top_left.y),
                    Point(self._top_left.x, self._bottom_right.y)
                ),
                "green"
            )

    def draw(self, x1, y1, x2, y2):
        Cell(Point(x1, y1), Point(x2, y2), self._master, self.walls)._draw()

    def draw_move(self, to_cell, undo=False):
        if (
            self._master is None 
            or self._top_left is None 
            or self._bottom_right is None
            or to_cell._top_left is None
            or to_cell._bottom_right is None
        ):

            return

        color = 'red' if undo == False else 'grey'
        self_center = Point(
            (self._top_left.x + self._bottom_right.x) // 2,
            (self._top_left.y + self._bottom_right.y) // 2
        )
        to_cell_center = Point(
            (to_cell._top_left.x + to_cell._bottom_right.x) // 2,
            (to_cell._top_left.y + to_cell._bottom_right.y) // 2
        )

        self._master.draw_line(Line(self_center, to_cell_center), color)

