from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

win = Window(800, 600)

maze = Maze(Point(0, 0), 30, 60, Point(10, 10), win, 0)
maze.solve()

win.wait_for_close()


