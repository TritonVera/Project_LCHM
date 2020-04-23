#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:17 2020

@author: Григорий
@author: Ivan
"""
import sys  # System function
# import math

from PyQt5.QtWidgets import QApplication
from UI import DemoWindow as UI  # User interface classes
from Radiopulse import *
from ExciterObj import SignalCl

type_of_signal = "LNF"
app = QApplication(sys.argv)
ui = UI()

def close(): #Закрыть

    sys.exit()

def plotb(): #Построить
    
    """Вставка функции для реализации пачки радиоимпульсов"""
    global Time, Value, Value_I, Value_Q

    if ui.choose_panel.radio_radiobutton.isChecked():
        ui.plot_panel.draw_plot(radio.xpoints, radio.Ipoints, radio.Qpoints, radio.Zpoints)
    else:
        Time, Value, Value_I, Value_Q = radio_mod.Gen_Signal(
            ui.setup_panel.ku_i_spinbox.value(), type_of_signal)
        ui.plot_panel.draw_plot(Time, Value_I, Value_Q, Value)

def radio_push():
    ui.time_panel.time_stop_spinbox.setValue(20)
    ui.time_panel.time_start_spinbox.setValue(0)
    ui.setup_panel.time_spinbox.setVisible(1)
    ui.setup_panel.time_label.setVisible(1)
    ui.setup_panel.number_spinbox.setVisible(1)
    ui.setup_panel.number_label.setVisible(1)
    plotb()

def LNF(): #НЛЧМ
    global type_of_signal
    ui.time_panel.time_stop_spinbox.setValue(100)
    ui.time_panel.time_start_spinbox.setValue(0)
    ui.setup_panel.time_spinbox.setVisible(0)
    ui.setup_panel.time_label.setVisible(0)
    ui.setup_panel.number_spinbox.setVisible(0)
    ui.setup_panel.number_label.setVisible(0)
    if ui.choose_panel.nlchm_radiobutton.isChecked():
        type_of_signal = "NLNF"
    elif ui.choose_panel.lchm_radiobutton.isChecked():
        type_of_signal = "LNF"
    plotb()
    
def redraw_plot_time():
    ui.time_panel.time_start_spinbox.setMaximum(ui.time_panel.time_stop_spinbox.value() - 0.1)
    ui.time_panel.time_stop_spinbox.setMinimum(ui.time_panel.time_start_spinbox.value() + 0.1)
    if (ui.time_panel.auto_button.isChecked() == 0):
        start = ui.time_panel.time_start_spinbox.value()
        stop = ui.time_panel.time_stop_spinbox.value()
        if (stop > start):
            radio.time_configure(start_time = start, end_time = stop)
            radio_mod.Configure(Start = start, Stop = stop)
            plotb()

def redraw_plot():
    if (ui.setup_panel.divide_button.isChecked()):
        ui.setup_panel.ku_q_spinbox.setValue(ui.setup_panel.ku_i_spinbox.value())

    ui.setup_panel.pulse_spinbox.setMaximum(ui.setup_panel.period_spinbox.value())
    ui.setup_panel.period_spinbox.setMinimum(ui.setup_panel.pulse_spinbox.value())
    ui.setup_panel.period_spinbox.setMaximum(ui.setup_panel.time_spinbox.value() / 
                                             ui.setup_panel.number_spinbox.value())
    ui.setup_panel.time_spinbox.setMinimum(ui.setup_panel.period_spinbox.value() * 
                                           ui.setup_panel.number_spinbox.value())
    ui.setup_panel.number_spinbox.setMaximum(round(ui.setup_panel.time_spinbox.value() / 
                                             ui.setup_panel.period_spinbox.value()))

    if (ui.time_panel.auto_button.isChecked()):
        if (ui.choose_panel.radio_radiobutton.isChecked()):
            ui.time_panel.time_stop_spinbox.setValue(radio.xpoints[-1])
            ui.time_panel.time_start_spinbox.setValue(radio.xpoints[0])

        radio.configure(frequency = ui.setup_panel.f_spinbox.value(), 
                        amplify_i = ui.setup_panel.ku_i_spinbox.value(),
                        amplify_q = ui.setup_panel.ku_q_spinbox.value(),
                        length = ui.setup_panel.pulse_spinbox.value(),
                        period_pulse = ui.setup_panel.period_spinbox.value(),
                        number = ui.setup_panel.number_spinbox.value(),
                        period_packet = ui.setup_panel.time_spinbox.value())
        radio.auto(50, ui.time_panel.auto_spinbox.value())
        plotb()
    else:
        radio.configure(frequency = ui.setup_panel.f_spinbox.value(), 
                        amplify_i = ui.setup_panel.ku_i_spinbox.value(),
                        amplify_q = ui.setup_panel.ku_q_spinbox.value(),
                        length = ui.setup_panel.pulse_spinbox.value(),
                        period_pulse = ui.setup_panel.period_spinbox.value(),
                        number = ui.setup_panel.number_spinbox.value(),
                        period_packet = ui.setup_panel.time_spinbox.value())
        radio.time_configure()
        plotb()

def auto_but():
    if (ui.choose_panel.radio_radiobutton.isChecked()):
        if (ui.time_panel.auto_button.isChecked()):
            ui.time_panel.time_stop_spinbox.setEnabled(0)
            ui.time_panel.time_start_spinbox.setEnabled(0)
            ui.time_panel.auto_spinbox.setEnabled(1)
            ui.timer.start(20)
        else:
            ui.timer.stop()
            ui.time_panel.time_stop_spinbox.setEnabled(1)
            ui.time_panel.auto_spinbox.setEnabled(0)
            ui.time_panel.time_start_spinbox.setEnabled(1)

def div_but():
    if (ui.setup_panel.divide_button.isChecked()):
        ui.setup_panel.ku_q_spinbox.setVisible(0)
        ui.setup_panel.ku_q_label.setVisible(0)
        ui.setup_panel.ku_i_label.setText("Коэф. усиления")
    else:
        ui.setup_panel.ku_i_label.setText("Коэф. усиления I")
        ui.setup_panel.ku_q_label.setVisible(1)
        ui.setup_panel.ku_q_spinbox.setVisible(1)

#Привязка кнопок
ui.choose_panel.radio_radiobutton.toggled.connect(radio_push)
ui.choose_panel.lchm_radiobutton.toggled.connect(LNF)
ui.choose_panel.nlchm_radiobutton.toggled.connect(LNF)
ui.button_panel.exit_button.clicked.connect(close)
ui.time_panel.auto_button.toggled.connect(auto_but)
ui.setup_panel.divide_button.toggled.connect(div_but)

#Привязка изменения значения в спинбоксах
ui.setup_panel.ku_i_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.ku_q_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.f_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.time_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.pulse_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.period_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.number_spinbox.valueChanged.connect(redraw_plot)
ui.time_panel.time_stop_spinbox.valueChanged.connect(redraw_plot_time)
ui.time_panel.time_start_spinbox.valueChanged.connect(redraw_plot_time)

# Привязка таймера
ui.timer.timeout.connect(redraw_plot)

radio = Radiopulse()
radio_mod = SignalCl() 
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
