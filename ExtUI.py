import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QSizePolicy, QWidget, QGroupBox, QRadioButton, \
                            QVBoxLayout, QLabel, QHBoxLayout, QPushButton, \
                            QDoubleSpinBox
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#Класс графического полотна
class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None ,width = 4 ,height = 3 ,dpi = 100):

        fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)

        self.draw_plot()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def draw_plot(self, x_point = [], y_point = []):
        if (x_point != [] and y_point != []):
            self.axes.cla()
            self.axes.plot(x_point, y_point)
            self.draw()
        else:
            pass
            #self.axes.plot([0, 100], [0, 0], 'r')


class SetupWindow(QGroupBox):
    def __init__(self, parent = None):
        QGroupBox.__init__(self, parent)
        print(parent)
        self.setDisabled(1)


class MyLabel(QLabel):
    def __init__ (self, text = None, parent = None, subparent = None):
        QLabel.__init__(self, text, parent)
        self.subparent = subparent
        self.setMouseTracking(1)
        self.setup_window = SetupWindow(self.subparent)

    def mouseMoveEvent(self, event):
        posx = event.x()
        posy = event.y()
        #print("Координаты:\n x = %d  y = %d" % (posx, posy))

        if posx > 38 and posy > 3 and posy < 15:
            print("Координаты:\n x = %d  y = %d" % (posx, posy))
            position_x = self.x() + posx + 20
            position_y = self.y() + self.height() / 2
            self.setup_window.move(position_x, position_y)
            self.setup_window.setEnabled(1)
        else:
            print("Another")
            #del(self.setup_window);
