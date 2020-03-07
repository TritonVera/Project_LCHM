# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:10:12 2020

@author: Григорий
@author: Ivan
"""
from PyQt5 import uic
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QSizePolicy,\
                            QMessageBox, QWidget, QGroupBox, QRadioButton,\
                            QVBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

class DemoWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.max_pixel_size = 16777215
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Демонстрационная программа")
        self.create_ui()

    def create_ui(self):
        #Create and configure central widget
        self.main_widget = QWidget()
        self.main_widget.setMinimumSize(640, 480)
        self.main_widget.setGeometry(300, 300, 640, 480)
        self.setCentralWidget(self.main_widget)
        #print(self.centralWidget())

        #Create and configure packer
        self.main_grid = QGridLayout(self.main_widget)
        self.create_left_panel()
        self.create_plot_place()
        self.create_button_panel()
        self.main_widget.setLayout(self.main_grid)

    def create_left_panel(self):
        #Create main layout
        vertical_layout = QVBoxLayout(self.main_widget)

        #Create groupboxes
        exciter_box = QGroupBox(self.main_widget)
        amplifier_box = QGroupBox(self.main_widget)

        #Configure geometry
        exciter_box.setMinimumSize(250, 350)
        exciter_box.setMaximumSize(250, self.max_pixel_size)
        amplifier_box.setMinimumSize(250, 100)
        amplifier_box.setMaximumSize(250, 100)

        #Configure panel
        exciter_box.setTitle("Возбудитель")
        amplifier_box.setTitle("Усилитель мощности")

        #Make main layout packer
        inner_grid_layout = QGridLayout(exciter_box)
        inner_horizontal_layout = QGridLayout(amplifier_box)
        
        #Create radiobuttons
        lchm_radiobutton = QRadioButton("ЛЧМ", exciter_box)
        nlchm_radiobutton = QRadioButton("НЛЧМ", exciter_box)
        radio_radiobutton = QRadioButton("Пачка РИ", exciter_box)

        #Pack radiobuttons
        inner_grid_layout.addWidget(lchm_radiobutton, 0, 0)
        inner_grid_layout.addWidget(nlchm_radiobutton, 1, 0)
        inner_grid_layout.addWidget(radio_radiobutton, 2, 0)

        #Ending packers
        exciter_box.setLayout(inner_grid_layout)
        amplifier_box.setLayout(inner_horizontal_layout)

        vertical_layout.addWidget(exciter_box)
        vertical_layout.addWidget(amplifier_box)
        self.main_grid.addLayout(vertical_layout, 0, 0, -1, 2)

    def create_plot_place(self):                #TODO(Ivan): Create function
        pass

    def create_button_panel(self):              #TODO(Ivan): Create function
        pass

    def about(self):
        QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py demonstartion
Copyright 2020 Ivan Fomin, 2020 Grigory Galchenkov

This program is a demonstration of singal generator work.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                                )
