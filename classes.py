from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self, width, height):
        self.app = QApplication.instance()
        if not self.app:
            self.app = QApplication(sys.argv)

        super().__init__()
        self.setWindowTitle("Maze Solver")
        self.setGeometry(100, 100, width, height)


        self.lines = []
        self.line_colors = []

    def draw_line(self, line, fill_color="black"):
        self.lines.append(line)
        self.line_colors.append(fill_color)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)


        painter.fillRect(self.rect(), Qt.white)


        for i, line in enumerate(self.lines):
            line.draw(painter, self.line_colors[i])

    def closeEvent(self, event):
        event.accept()

    def wait_for_close(self):
        self.show()
        sys.exit(self.app.exec_())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, painter, fill_color="black"):
        color_map = {
            "black": QColor(0, 0, 0),
            "red": QColor(255, 0, 0),
            "blue": QColor(0, 0, 255),
            "green": QColor(0, 255, 0),
            "yellow": QColor(255, 255, 0),
            "purple": QColor(128, 0, 128),
            "orange": QColor(255, 165, 0),
            "gray": QColor(128, 128, 128),
            "white": QColor(255, 255, 255)
        }

        color = color_map.get(fill_color.lower(), QColor(0, 0, 0))

        pen = QPen(color, 2)
        painter.setPen(pen)

        painter.drawLine(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            print(f"  Drawing left wall from ({self._x1},{self._y1}) to ({self._x1},{self._y2})")
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall)

        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall)

        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, painter: QPainter, to_cell, undo=False):
        x1 = self.col * self.size + self.size // 2
        y1 = self.row * self.size + self.size // 2
        x2 = to_cell.col * to_cell.size + to_cell.size // 2
        y2 = to_cell.row * to_cell.size + to_cell.size // 2

        color = QColor(128, 128, 128) if undo else QColor(255, 0, 0)
        pen = QPen(color, 2)
        painter.setPen(pen)

        painter.drawLine(x1, y1, x2, y2)
        print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}, undo: {undo}")

    class Maze:
        def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        )

        def _create_cells(self):
