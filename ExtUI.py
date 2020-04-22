import numpy as np

from PyQt5.QtWidgets import QSizePolicy, QWidget, QGroupBox, QRadioButton, \
                            QVBoxLayout, QLabel, QHBoxLayout, QPushButton, \
                            QDoubleSpinBox
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from qwt import QwtPlot, QwtPlotCurve

#Класс графического полотна
class PlotPanel(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        vertical_layout = QVBoxLayout()

        self.plot_up = QwtPlot(self)
        self.plot_down = QwtPlot(self)
        self.line_i = QwtPlotCurve()
        self.line_q = QwtPlotCurve()
        self.line_z = QwtPlotCurve()
        self.draw_plot()

        vertical_layout.addWidget(self.plot_up)
        vertical_layout.addWidget(self.plot_down)

        self.setLayout(vertical_layout)

    def draw_plot(self, x_points = [], i_points = [], q_points = [], z_points = []):
        x_list = np.asarray(x_points)

        i_list = np.asarray(i_points)
        q_list = np.asarray(q_points)
        z_list = np.asarray(z_points)

        z_color = QColor(0, 255, 0)
        z_pen = QPen(z_color)
        z_pen.setWidth(2)

        q_color = QColor(255, 0, 0)
        q_pen = QPen(q_color)
        q_pen.setWidth(2)

        i_color = QColor(255, 0, 255)
        i_pen = QPen(i_color)
        i_pen.setWidth(2)

        self.line_i.setData(x_list, i_list)
        self.line_i.setPen(i_pen)
        self.line_i.attach(self.plot_down)

        self.line_q.setData(x_list, q_list)
        self.line_q.setPen(q_pen)
        self.line_q.attach(self.plot_down)

        self.line_z.setData(x_list, z_list)
        self.line_z.setPen(z_pen)
        self.line_z.attach(self.plot_down)
        self.plot_down.replot()
        self.plot_down.show()
        self.plot_up.replot()
        self.plot_up.show()


# class SetupWindow(QGroupBox):
#     def __init__(self, parent = None):
#         QGroupBox.__init__(self, parent)
#         print(parent)


# class MyLabel(QLabel):
#     def __init__ (self, text = None, parent = None, subparent = None):
#         QLabel.__init__(self, text, parent)
#         self.subparent = subparent
#         self.setMouseTracking(1)
#         self.setup_window = SetupWindow(self.subparent)

#     def mouseMoveEvent(self, event):
#         posx = event.x()
#         posy = event.y()
#         #print("Координаты:\n x = %d  y = %d" % (posx, posy))

#         if posx > 38 and posy > 3 and posy < 15:
#             print("Координаты:\n x = %d  y = %d" % (posx, posy))
#             position_x = self.x() + posx + 20
#             position_y = self.y() + self.height() / 2
#             self.setup_window.setGeometry(300, 100, 50, 100)
#             self.setup_window.setEnabled(1)
#         else:
#             print("Another")
#             if (self.setup_window.isEnabled()):
#                 self.setup_window.setEnabled(0)
