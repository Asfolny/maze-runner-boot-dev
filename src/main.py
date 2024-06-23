from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

win = Window(800, 800)

maze = Maze(Point(0, 0), 45, 45, Point(15, 15), win)
maze.solve()

win.wait_for_close()

