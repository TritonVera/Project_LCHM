#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:17 2020

@author: Григорий
@author: Ivan
"""
import sys                            #System function

from PyQt5.QtWidgets import QApplication
from UI import DemoWindow as UI  #User interface classes
from Radiopulse import *
from ExciterObj import SignalCl

type_of_signal = "LNF"
app = QApplication(sys.argv)
ui = UI()

def close(): #Закрыть

    sys.exit()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""

    if ui.choose_panel.radio_radiobutton.isChecked():
        ui.plot_panel.draw_plot(radio.xpoints, radio.Ipoints, radio.Qpoints, radio.Zpoints)
    else:
        Time, Value, Value_I, Value_Q = radio_mod.Gen_Signal(
            ui.setup_panel.ku_i_spinbox.value(), type_of_signal)
        ui.plot_panel.draw_plot(Time, Value_I, Value_Q, Value)

def radio_push():
    ui.time_panel.time_stop_spinbox.setValue(20)
    ui.time_panel.time_start_spinbox.setValue(0)
    plotb()

def LNF(): #НЛЧМ
    global type_of_signal
    ui.time_panel.time_stop_spinbox.setValue(100)
    ui.time_panel.time_start_spinbox.setValue(0)
    if ui.choose_panel.nlchm_radiobutton.isChecked():
        type_of_signal = "NLNF"
    elif ui.choose_panel.lchm_radiobutton.isChecked():
        type_of_signal = "LNF"
    plotb()
    
def redraw_plot_time():
    start = ui.time_panel.time_start_spinbox.value()
    stop = ui.time_panel.time_stop_spinbox.value()
    if (stop < start):
        ui.time_panel.time_stop_spinbox.setValue(
            ui.time_panel.time_start_spinbox.value() + 1)
        ui.time_panel.time_start_spinbox.setValue(
            ui.time_panel.time_stop_spinbox.value() - 1)
    radio.time_configure(start_time = start, end_time = stop)
    radio_mod.Configure(Start = start, Stop = stop)
    plotb()

def redraw_plot():
    if (ui.time_panel.auto_button.isChecked()):
        radio.auto_configure(frequency = ui.setup_panel.f_spinbox.value(), 
                             amplify_i = ui.setup_panel.ku_i_spinbox.value(),
                             amplify_q = ui.setup_panel.ku_q_spinbox.value())
        radio.auto(50, 15)
        plotb()
    else:
        radio.configure(frequency = ui.setup_panel.f_spinbox.value(), 
                        amplify_i = ui.setup_panel.ku_i_spinbox.value(),
                        amplify_q = ui.setup_panel.ku_q_spinbox.value())
        plotb()

def auto_but():
    if (ui.choose_panel.radio_radiobutton.isChecked()):
        if (ui.time_panel.auto_button.isChecked()):
            ui.time_panel.time_stop_spinbox.setEnabled(0)
            ui.time_panel.time_start_spinbox.setEnabled(0)
            ui.timer.start(20)
        else:
            ui.timer.stop()
            ui.time_panel.time_stop_spinbox.setEnabled(1)
            ui.time_panel.time_start_spinbox.setEnabled(1)
            stop = radio.xpoints[len(radio.xpoints) - 1]
            start = radio.xpoints[0]
            ui.time_panel.time_stop_spinbox.setValue(stop)
            ui.time_panel.time_start_spinbox.setValue(start)

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
ui.choose_panel.radio_radiobutton.toggled.connect(radio_push)
ui.choose_panel.lchm_radiobutton.toggled.connect(LNF)
ui.choose_panel.nlchm_radiobutton.toggled.connect(LNF)
ui.button_panel.exit_button.clicked.connect(close)
ui.button_panel.plot_button.clicked.connect(plotb)
ui.time_panel.auto_button.toggled.connect(auto_but)

#Привязка изменения значения в спинбоксах
ui.setup_panel.ku_i_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.ku_q_spinbox.valueChanged.connect(redraw_plot)
ui.setup_panel.f_spinbox.valueChanged.connect(redraw_plot)
ui.time_panel.time_stop_spinbox.valueChanged.connect(redraw_plot_time)
ui.time_panel.time_start_spinbox.valueChanged.connect(redraw_plot_time)

# Привязка таймера
ui.timer.timeout.connect(redraw_plot)

radio = Radiopulse()
radio_mod = SignalCl() 
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
