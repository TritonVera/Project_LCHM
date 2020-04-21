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
from threading import Thread

type_of_signal = "LNF"

def close(): #Закрыть

    sys.exit()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""

    if ui.choose_panel.radio_radiobutton.isChecked():
        ui.plot_panel.draw_plot(radio.xpoints, radio.Ipoints, radio.Qpoints, radio.Zpoints)
    else:
        Time, Value, Value_I, Value_Q = radio_mod.Gen_Signal(
            ui.setup_panel.ku_spinbox.value(), type_of_signal)
        ui.plot_panel.draw_plot(Time, Value_I, Value_Q, Value)

def NLNF(): #НЛЧМ

    if ui.choose_panel.nlchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "NLNF"
    plotb()

def LNF(): #ЛЧМ

    if ui.choose_panel.lchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "LNF"
    plotb()

app = QApplication(sys.argv)
ui = UI()
    
def redraw_plot_start():
    start = ui.time_panel.time_start_spinbox.value()
    stop = ui.time_panel.time_stop_spinbox.value()
    if (stop < start):
        ui.time_panel.time_stop_spinbox.setValue(
            ui.time_panel.time_start_spinbox.value() + 1)
    radio.time_configure(start_time = start, end_time = stop)
    radio_mod.Configure(Start = start, Stop = stop)
    plotb()

def redraw_plot_stop():
    start = ui.time_panel.time_start_spinbox.value()
    stop = ui.time_panel.time_stop_spinbox.value()
    if (stop < start):
        ui.time_panel.time_start_spinbox.setValue(
            ui.time_panel.time_stop_spinbox.value() - 1)
    radio.time_configure(start_time = start, end_time = stop)
    radio_mod.Configure(Start = start,Stop = stop)
    plotb()

def redraw_plot_amplify():
    amplify = ui.setup_panel.ku_spinbox.value()
    radio.configure(amplify = amplify)
    plotb()

def redraw_plot_frequence():
    freq = ui.setup_panel.f_spinbox.value()
    radio.configure(frequency = freq)
    plotb()

def auto():
    radio.auto()
    plotb()

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
ui.choose_panel.radio_radiobutton.toggled.connect(plotb)
ui.choose_panel.lchm_radiobutton.toggled.connect(LNF)
ui.choose_panel.nlchm_radiobutton.toggled.connect(NLNF)
ui.button_panel.exit_button.clicked.connect(close)
ui.button_panel.plot_button.clicked.connect(plotb)
# ui.time_panel.auto_button.toggled.connect(auto)
ui.time_panel.auto_button.clicked.connect(auto)

#Привязка изменения значения в спинбоксах
ui.setup_panel.ku_spinbox.valueChanged.connect(redraw_plot_amplify)
ui.setup_panel.f_spinbox.valueChanged.connect(redraw_plot_frequence)
ui.time_panel.time_stop_spinbox.valueChanged.connect(redraw_plot_stop)
ui.time_panel.time_start_spinbox.valueChanged.connect(redraw_plot_start)

radio = Radiopulse()
radio_mod = SignalCl() 
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
