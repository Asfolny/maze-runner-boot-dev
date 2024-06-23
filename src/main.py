from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

win = Window(800, 600)

maze = Maze(Point(5, 5), 3, 3, Point(100, 100), win)
maze.solve()

win.wait_for_close()


