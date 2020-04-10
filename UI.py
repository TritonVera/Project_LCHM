# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:10:12 2020

@author: Григорий
@author: Ivan
"""

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QSizePolicy, \
                            QMessageBox, QWidget, QGroupBox, QRadioButton, \
                            QVBoxLayout, QLabel, QHBoxLayout, QPushButton, \
                            QDoubleSpinBox
from PyQt5.QtCore import Qt
from ExtUI import MyLabel, PlotCanvas, SetupWindow

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

        up_plot_place = self.create_plot_place()
        self.main_grid.addWidget(up_plot_place, 0, 1, 1, 2)

        time_panel = self.create_time_panel()
        self.main_grid.addWidget(time_panel, 1, 1)

        button_panel = self.create_button_panel()
        self.main_grid.addWidget(button_panel, 1, 2)

        self.main_widget.setLayout(self.main_grid)


    def create_main_widget(self):
        self.main_widget = QWidget()
        self.main_widget.setMinimumSize(800, 640)
        self.main_widget.setGeometry(200, 200, 800, 640)
        self.setCentralWidget(self.main_widget)

    def create_left_panel(self):
        #Create main widget and layout
        left_widget = QWidget(self.main_widget)
        vertical_layout = QVBoxLayout()

        #Create groupboxes
        exciter_box = QGroupBox(left_widget)
        amplifier_box = QGroupBox(left_widget)

        #Configure geometry
        exciter_box.setMinimumSize(250, 345)
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
        #self.lchm_radiobutton.setDisabled(1)
        #self.nlchm_radiobutton.setDisabled(1)

        #Create label
        ku_label = QLabel("Коэф. усиления:", amplifier_box)
        # setup_radio_label = MyLabel("Настроить", exciter_box, self.main_widget)
        # setup_radio_label.setAlignment(Qt.AlignRight)

        #Create spinbox
        self.ku_spinbox = QDoubleSpinBox(amplifier_box)

        #Configure spinbox
        self.ku_spinbox.setRange(0.1, 100)
        self.ku_spinbox.setSuffix(" раз")
        self.ku_spinbox.setValue(1)
        self.ku_spinbox.setSingleStep(0.1)

        #Pack radiobuttons
        inner_grid_layout.addWidget(self.lchm_radiobutton, 0, 0)
        inner_grid_layout.addWidget(self.nlchm_radiobutton, 1, 0)
        inner_grid_layout.addWidget(self.radio_radiobutton, 2, 0)
        # inner_grid_layout.addWidget(setup_radio_label, 2, 1)

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
        vertical_layout = QVBoxLayout()

        self.plot = PlotCanvas(plot_widget)
        vertical_layout.addWidget(self.plot)

        plot_widget.setLayout(vertical_layout)
        return plot_widget

    def create_time_panel(self):
        time_changed_widget = QWidget(self.main_widget)
        simple_layout = QHBoxLayout()

        time_box = QGroupBox(time_changed_widget)
        time_box.setMinimumSize(320, 100)
        time_box.setSizePolicy(QSizePolicy.Expanding,
                               QSizePolicy.Fixed)
        time_box.setTitle("Время")

        grid_manage = QGridLayout(time_box)
 
        #Create box elements
        time_start_label = QLabel("Начальная точка", time_box)
        time_stop_label = QLabel("Конечная точка", time_box)
        self.time_start_spinbox = QDoubleSpinBox(time_box)
        self.time_stop_spinbox = QDoubleSpinBox(time_box)

        #Configure spinboxes
        self.time_start_spinbox.setRange(0.00, 1000)
        self.time_stop_spinbox.setRange(0.1, 1000.1)
        self.time_stop_spinbox.setValue(100.0)

        #Add elememts to grid packer
        grid_manage.addWidget(time_start_label, 0, 0)
        grid_manage.addWidget(time_stop_label, 0, 1)
        grid_manage.addWidget(self.time_start_spinbox, 1, 0)
        grid_manage.addWidget(self.time_stop_spinbox, 1, 1)

        time_box.setLayout(grid_manage)
        simple_layout.addWidget(time_box)
        time_changed_widget.setLayout(simple_layout)

        return time_changed_widget

    def create_button_panel(self):
        button_widget = QWidget(self.main_widget)
        simple_layout = QHBoxLayout()

        button_box = QGroupBox(button_widget)
        button_box.setMinimumSize(120, 100)
        button_box.setMaximumSize(120, 100)
        button_box.setTitle("Управление")

        box_layout = QVBoxLayout(button_widget)

        # Create buttons
        self.plot_button = QPushButton("Построить", button_box)
        self.exit_button = QPushButton("Выход", button_box)

        # Add to layout
        box_layout.addWidget(self.plot_button)
        box_layout.addWidget(self.exit_button)
        button_box.setLayout(box_layout)

        # Place main layout
        simple_layout.addWidget(button_box)
        button_widget.setLayout(simple_layout)

        return button_widget


    def about(self):
        QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py demonstartion
Copyright 2020 Ivan Fomin, 2020 Grigory Galchenkov

This program is a demonstration of excite signal in receiver.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                                )
