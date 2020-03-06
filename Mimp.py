# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:10:12 2020

@author: Григорий
"""
from PyQt5.QtWidgets import  QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5 import uic
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ExciterObj import *
from Radiopulse import *

class PlotCanvas(FigureCanvas):

    def __init__(self,parent ,width ,height ,dpi):

        fig = Figure(figsize=(width, height), dpi = float(dpi))
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



    def plot(self, tm = Time, sgn = Sign):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(tm,sgn)
        self.draw()
        
