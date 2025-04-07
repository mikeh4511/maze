from PyQt5.QtWidgets import QApplication
import sys
import time

from classes import *

def main():
    app = QApplication(sys.argv)

    win = Window(800, 600)
    win.show()

    x1, y1 = 100, 100
    x2, y2 = 200, 200

    maze = Maze(x1, y1, 20, 20, 20, 20, win)


    win.wait_for_close()





    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
