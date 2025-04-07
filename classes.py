from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import time
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

    def redraw(self):
        self.update()


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
    def __init__(self, x1, y1, x2, y2, win, row =0, col=0):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

        self.row = row
        self.col = col
        self.size = x2 - x1

    def draw(self):
        if self.has_left_wall:
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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []

            for row in range(self.num_rows):
                x1 = self.x1 + (col * self.cell_size_x)
                y1 = self.y1 + (row * self.cell_size_y)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1, y1, x2, y2, self.win, row, col)
                column.append(cell)

            self._cells.append(column)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):

        cell = self._cells[i][j]

        cell.draw()

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
