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
from PyQt5.QtCore import Qt, QTimer
from ExtUI import PlotPanel
import Radiopulse

MAX_PIXEL_SIZE = 16777215

#Класс главного окна
class DemoWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Демонстрационная программа")
        self.timer = QTimer()
        self.create_ui()

    def create_ui(self):
        #Create and configure central widget
        self.create_main_widget()

        #Create and configure packer
        self.main_grid = QGridLayout(self.main_widget)

        self.choose_panel = ChoosePanel(self.main_widget)
        self.main_grid.addWidget(self.choose_panel, 0, 0)

        self.setup_panel = SetupPanel(self.main_widget)
        self.main_grid.addWidget(self.setup_panel, 1, 0, -1, 1)

        self.plot_panel = PlotPanel(self.main_widget)
        self.main_grid.addWidget(self.plot_panel, 0, 1, 2, -1)

        self.time_panel = TimePanel(self.main_widget)
        self.main_grid.addWidget(self.time_panel, 2, 1)

        self.button_panel = ButtonPanel(self.main_widget)
        self.main_grid.addWidget(self.button_panel, 2, 2)

        self.main_widget.setLayout(self.main_grid)


    def create_main_widget(self):
        self.main_widget = QWidget()
        self.main_widget.setMinimumSize(800, 640)
        self.main_widget.setGeometry(0, 0, 800, 640)
        self.setCentralWidget(self.main_widget)


    def about(self):
        QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py demonstartion
Copyright 2020 Ivan Fomin, 2020 Grigory Galchenkov

This program is a demonstration of excite signal in receiver.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                                )

class ChoosePanel(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        QWidget.setFixedSize(self, 310, 120)

        #Create main widget and layout
        vertical_layout = QVBoxLayout()

        #Create groupboxes
        exciter_box = QGroupBox(self)
        exciter_box.setMinimumSize(310, 120)
        exciter_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        exciter_box.setTitle("Возбудитель")

        #Make main layout packer
        inner_grid_layout = QGridLayout(exciter_box)
        
        #Create radiobuttons
        self.lchm_radiobutton = QRadioButton("ЛЧМ", exciter_box)
        self.nlchm_radiobutton = QRadioButton("НЛЧМ", exciter_box)
        self.radio_radiobutton = QRadioButton("Пачка РИ", exciter_box)

        #Pack radiobuttons
        inner_grid_layout.addWidget(self.lchm_radiobutton, 0, 0)
        inner_grid_layout.addWidget(self.nlchm_radiobutton, 1, 0)
        inner_grid_layout.addWidget(self.radio_radiobutton, 2, 0)

        #Ending packers
        exciter_box.setLayout(inner_grid_layout)
        vertical_layout.addWidget(exciter_box)
        self.setLayout(vertical_layout)


class SetupPanel(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        #Create main widget and layout
        vertical_layout = QVBoxLayout()

        #Create groupboxes
        setup_box = QGroupBox(self)
        setup_box.setMinimumSize(300, 100)
        setup_box.setGeometry(0, 0, 300, 100)
        setup_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        setup_box.setTitle("Параметры сигнала")

        #Make main layout packer
        inner_grid_layout = QGridLayout(setup_box)
        
        # Create elements
        self.ku_i_label = QLabel("Коэф. усиления:", setup_box)
        self.ku_i_spinbox = QDoubleSpinBox(setup_box)
        self.divide_button = QPushButton("Совместное усиление квадратур", setup_box)
        self.ku_q_label = QLabel("Коэф. усиления Q:", setup_box)
        self.ku_q_spinbox = QDoubleSpinBox(setup_box)
        f_label = QLabel("Частота:", setup_box)
        self.f_spinbox = QDoubleSpinBox(setup_box)
        self.time_label = QLabel("Период пачки:", setup_box)
        self.time_spinbox = QDoubleSpinBox(setup_box)
        self.period_label = QLabel("Период импульсов:", setup_box)
        self.period_spinbox = QDoubleSpinBox(setup_box)
        self.number_label = QLabel("Число импульсов:", setup_box)
        self.number_spinbox = QDoubleSpinBox(setup_box)
        self.pulse_label = QLabel("Длительность импульса:", setup_box)
        self.pulse_spinbox = QDoubleSpinBox(setup_box)

        # Configure spinboxes
        self.ku_i_spinbox.setValue(1)
        self.ku_i_spinbox.setRange(0, 100)
        self.ku_i_spinbox.setSingleStep(0.1)
        self.ku_q_spinbox.setValue(1)
        self.ku_q_spinbox.setRange(0, 100)
        self.ku_q_spinbox.setSingleStep(0.1)

        self.f_spinbox.setSuffix(" МГц")
        self.f_spinbox.setValue(2)
        self.f_spinbox.setRange(0.1, 100)
        self.f_spinbox.setSingleStep(0.1)

        self.time_spinbox.setValue(100)
        self.time_spinbox.setSuffix(" мкс")
        self.time_spinbox.setSingleStep(1)
        self.time_spinbox.setRange(1, 1000)

        self.number_spinbox.setValue(10)
        self.number_spinbox.setSingleStep(1)
        self.number_spinbox.setRange(1, 100)

        self.period_spinbox.setValue(4)
        self.period_spinbox.setRange(0.01, 100)
        self.period_spinbox.setSuffix(" мкс")
        self.period_spinbox.setSingleStep(0.1)

        self.pulse_spinbox.setValue(2)
        self.pulse_spinbox.setRange(0.01, 100)
        self.pulse_spinbox.setSuffix(" мкс")
        self.pulse_spinbox.setSingleStep(0.1)

        self.time_spinbox.setVisible(0)
        self.time_label.setVisible(0)
        self.number_spinbox.setVisible(0)
        self.number_label.setVisible(0)
        self.divide_button.setCheckable(1)

        # Pack elements
        inner_grid_layout.addWidget(self.ku_i_label, 0, 0)
        inner_grid_layout.addWidget(self.ku_i_spinbox, 0, 1)
        inner_grid_layout.addWidget(self.divide_button, 1, 0, 1, -1)
        inner_grid_layout.addWidget(self.ku_q_label, 2, 0)
        inner_grid_layout.addWidget(self.ku_q_spinbox, 2, 1)
        inner_grid_layout.addWidget(f_label, 3, 0)
        inner_grid_layout.addWidget(self.f_spinbox, 3, 1)
        inner_grid_layout.addWidget(self.time_label, 4, 0)
        inner_grid_layout.addWidget(self.time_spinbox, 4, 1)
        inner_grid_layout.addWidget(self.period_label, 5, 0)
        inner_grid_layout.addWidget(self.period_spinbox, 5, 1)
        inner_grid_layout.addWidget(self.number_label, 6, 0)
        inner_grid_layout.addWidget(self.number_spinbox, 6, 1)
        inner_grid_layout.addWidget(self.pulse_label, 7, 0)
        inner_grid_layout.addWidget(self.pulse_spinbox, 7, 1)

        #Ending packers
        setup_box.setLayout(inner_grid_layout)

        vertical_layout.addWidget(setup_box)
        self.setLayout(vertical_layout)


class TimePanel(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        simple_layout = QHBoxLayout()

        time_box = QGroupBox(self)
        time_box.setMinimumSize(320, 135)
        time_box.setSizePolicy(QSizePolicy.Expanding,
                               QSizePolicy.Fixed)
        time_box.setTitle("Время")

        grid_manage = QGridLayout(time_box)

       #Create box elements
        time_start_label = QLabel("Начальная точка", time_box)
        time_stop_label = QLabel("Конечная точка", time_box)
        self.time_start_spinbox = QDoubleSpinBox(time_box)
        self.time_stop_spinbox = QDoubleSpinBox(time_box)
        self.auto_button = QPushButton("Запуск", time_box)
        self.auto_spinbox = QDoubleSpinBox(time_box)

        #Configure elements
        self.time_start_spinbox.setRange(0.0, 1000000)
        self.time_start_spinbox.setSingleStep(0.1)
        self.time_start_spinbox.setSuffix(" мкс")
        self.time_stop_spinbox.setRange(0.1, 1000000.1)
        self.time_stop_spinbox.setSingleStep(0.1)
        self.time_stop_spinbox.setSuffix(" мкс")
        self.time_stop_spinbox.setValue(100.0)
        self.auto_button.setCheckable(1)
        self.auto_spinbox.setRange(0.0, 1000)
        self.auto_spinbox.setValue(10.0)
        self.auto_spinbox.setSingleStep(1)
        self.auto_spinbox.setEnabled(0)
        self.auto_spinbox.setSuffix(" мкс/c")

        #Add elememts to grid packer
        grid_manage.addWidget(time_start_label, 0, 0)
        grid_manage.addWidget(time_stop_label, 0, 1)
        grid_manage.addWidget(self.time_start_spinbox, 1, 0)
        grid_manage.addWidget(self.time_stop_spinbox, 1, 1)
        grid_manage.addWidget(self.auto_button, 2, 0)
        grid_manage.addWidget(self.auto_spinbox, 2, 1)

        time_box.setLayout(grid_manage)
        simple_layout.addWidget(time_box)
        self.setLayout(simple_layout)

class ButtonPanel(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setMinimumSize(120, 150)
        self.setSizePolicy(QSizePolicy.Fixed,
                           QSizePolicy.Fixed)

        simple_layout = QHBoxLayout()
        button_box = QGroupBox(self)
        button_box.setTitle("Управление")
        box_layout = QVBoxLayout(button_box)

        # Create buttons
#        self.plot_button = QPushButton("Построить", button_box)
        self.exit_button = QPushButton("Выход", button_box)

        # Add to layout
#        box_layout.addWidget(self.plot_button)
        box_layout.addWidget(self.exit_button)
        button_box.setLayout(box_layout)

        # Place main layout
        simple_layout.addWidget(button_box)
        self.setLayout(simple_layout)
