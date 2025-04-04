from PyQt5.QtWidgets import QApplication
import sys

from classes import *

def main():
    app = QApplication(sys.argv)

    win = Window(800, 600)
    win.show()

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 300)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p1, p4)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "black")

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
