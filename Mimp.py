# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:10:12 2020

@author: Григорий
@author: Ivan
"""
from PyQt5 import uic
import matplotlib
import sys

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QApplication, QMainWindow,\
                            QMenu, QVBoxLayout, QSizePolicy,\
                            QMessageBox, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ExciterObj import *
from Radiopulse import *

class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None ,width = 4 ,height = 3 ,dpi = 1000,
                 x_points = None, y_points = None):

        fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        self.x_points = x_points
        self.y_points = y_points

        self.plot()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self):
        pass

class MakePlot(PlotCanvas):
    """Simple canvas with a sine plot."""
    def __init__(self, *args, **kwargs):
        PlotCanvas.__init__(self, *args, **kwargs)

    def plot(self):
        self.axes.plot(self.x_points, self.y_points)

