from PyQt5.QtWidgets import QApplication
import sys

from classes import *

def main():
    app = QApplication(sys.argv)

    win = Window(800, 600)
    win.show()

    x1, y1 = 100, 100
    x2, y2 = 200, 200

    cell1 = Cell(x1, y1, x2, y2, win)
    cell2 = Cell(250, 100, 350, 200, win)

    cell2.has_left_wall = False
    cell2.draw()

    cell1.draw()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
