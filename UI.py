# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:10:12 2020

@author: Григорий
@author: Ivan
"""
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QSizePolicy, \
                            QMessageBox, QWidget, QGroupBox, QRadioButton, \
                            QVBoxLayout, QLabel, QHBoxLayout, QPushButton, \
                            QDoubleSpinBox
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#Класс графического полотна
class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None ,width = 5 ,height = 3 ,dpi = 100):

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
            self.axes.plot([0, 100], [0, 0], 'r')

#Класс главного окна
class DemoWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.max_pixel_size = 16777215
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Демонстрационная программа")
        self.create_ui()

    def create_ui(self):
        #Create and configure central widget
        self.create_main_widget()

        #Create and configure packer
        self.main_grid = QGridLayout(self.main_widget)

        left_panel = self.create_left_panel()
        self.main_grid.addWidget(left_panel, 0, 0, 2, 1)

        plot_place = self.create_plot_place()
        self.main_grid.addWidget(plot_place, 0, 1, 1, 2)

        time_panel = self.create_button_panel()
        self.main_grid.addWidget(time_panel, 1, 1)

        self.main_widget.setLayout(self.main_grid)

    def create_main_widget(self):
        self.main_widget = QWidget()
        self.main_widget.setMinimumSize(640, 480)
        self.main_widget.setGeometry(300, 300, 640, 480)
        self.setCentralWidget(self.main_widget)

    def create_left_panel(self):
        #Create main widget and layout
        left_widget = QWidget(self.main_widget)
        vertical_layout = QVBoxLayout(self.main_widget)

        #Create groupboxes
        exciter_box = QGroupBox(left_widget)
        amplifier_box = QGroupBox(left_widget)

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
        inner_horizontal_layout = QHBoxLayout(amplifier_box)
        
        #Create radiobuttons
        self.lchm_radiobutton = QRadioButton("ЛЧМ", exciter_box)
        self.nlchm_radiobutton = QRadioButton("НЛЧМ", exciter_box)
        self.radio_radiobutton = QRadioButton("Пачка РИ", exciter_box)

        #Configure radiobuttons
        self.radio_radiobutton.setChecked(1)
        self.lchm_radiobutton.setDisabled(1)
        self.nlchm_radiobutton.setDisabled(1)

        #Create label
        ku_label = QLabel("Коэф. усиления:", amplifier_box)

        #Create spinbox
        self.ku_spinbox = QDoubleSpinBox(amplifier_box)

        #Configure spinbox
        self.ku_spinbox.setMinimum(0.01)
        self.ku_spinbox.setMaximum(100)
        self.ku_spinbox.setSuffix(" раз")

        #Pack radiobuttons
        inner_grid_layout.addWidget(self.lchm_radiobutton, 0, 0)
        inner_grid_layout.addWidget(self.nlchm_radiobutton, 1, 0)
        inner_grid_layout.addWidget(self.radio_radiobutton, 2, 0)

        #Pack label
        inner_horizontal_layout.addWidget(ku_label)
        inner_horizontal_layout.addWidget(self.ku_spinbox)

        #Ending packers
        exciter_box.setLayout(inner_grid_layout)
        amplifier_box.setLayout(inner_horizontal_layout)

        vertical_layout.addWidget(exciter_box)
        vertical_layout.addWidget(amplifier_box)
        left_widget.setLayout(vertical_layout)
        return left_widget

    def create_plot_place(self):
        plot_widget = QWidget(self.main_widget)
        horizontal_layout = QHBoxLayout(plot_widget)

        self.plot = PlotCanvas(plot_widget)
        horizontal_layout.addWidget(self.plot)

        plot_widget.setLayout(horizontal_layout)
        return plot_widget

    def create_button_panel(self):              #TODO(Ivan): Create function
        time_changed_widget = QWidget(self.main_widget)
        simple_layout = QHBoxLayout(time_changed_widget)

        time_box = QGroupBox(time_changed_widget)
        time_box.setMinimumSize(450, 100)
        time_box.setMaximumSize(self.max_pixel_size, 100)

        self.time_start_spinbox = QDoubleSpinBox(time_box)
        self.time_stop_spinbox = QDoubleSpinBox(time_box)

        simple_layout.addWidget(time_box)

        time_changed_widget.setLayout(simple_layout)

        return time_changed_widget

    def about(self):
        QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py demonstartion
Copyright 2020 Ivan Fomin, 2020 Grigory Galchenkov

This program is a demonstration of excite signal in receiver.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                                )
