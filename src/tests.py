import unittest
from maze import Maze
from point import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, Point(10, 10))
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )


        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()

