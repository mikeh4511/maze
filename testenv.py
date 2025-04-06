from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QRect

# Mock Cell class for testing.
class Cell:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

    def draw_move(self, painter: QPainter, to_cell, undo=False):
        x1 = self.col * self.size + self.size // 2
        y1 = self.row * self.size + self.size // 2
        x2 = to_cell.col * to_cell.size + to_cell.size // 2
        y2 = to_cell.row * to_cell.size + to_cell.size // 2

        color = QColor(128, 128, 128) if undo else QColor(255, 0, 0)
        pen = QPen(color, 2)
        painter.setPen(pen)

        painter.drawLine(x1, y1, x2, y2)

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cell1 = Cell(2, 3, 50)  # Example cell 1 at (row=2, col=3), size=50
        self.cell2 = Cell(3, 4, 50)  # Example cell 2 at (row=3, col=4), size=50

    def paintEvent(self, event):
        painter = QPainter(self)
        # Draw a red line (undo=False)
        self.cell1.draw_move(painter, self.cell2, undo=False)

        # Draw a gray line (undo=True) between two other cells (you can adjust their values)
        another_cell = Cell(4, 5, 50)
        self.cell2.draw_move(painter, another_cell, undo=True)

        painter.end()

    def draw_move(self, painter: QPainter, to_cell, undo=False):
        x1 = self.col * self.size + self.size // 2
        y1 = self.row * self.size + self.size // 2
        x2 = to_cell.col * to_cell.size + to_cell.size // 2
        y2 = to_cell.row * to_cell.size + to_cell.size // 2

        color = QColor(128, 128, 128) if undo else QColor(255, 0, 0)
        pen = QPen(color, 2)
        painter.setPen(pen)

        painter.drawLine(x1, y1, x2, y2)

app = QApplication([])
window = TestWidget()
window.resize(400, 400)
window.show()
app.exec_()
