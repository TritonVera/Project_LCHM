#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:17 2020

@author: Григорий
@author: Ivan
"""
import sys                            #System function
import UI                             #User interface classes

from PyQt5.QtWidgets import QApplication
from Radiopulse import *
from ExciterObj import SignalCl                #TODO(Григорий): Make refactoring

type_of_signal = "LNF"

def close(): #Закрыть

    sys.exit()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""

    if ui.left_panel.radio_radiobutton.isChecked():
        #radio.send_test()
        ui.plot_panel.plot.draw_plot(radio.xpoints, radio.Ipoints, radio.Qpoints, radio.Zpoints)
    else:
        Time, Value, Value_I, Value_Q = radio_mod.Gen_Signal(
            ui.left_panel.ku_spinbox.value(), type_of_signal)
        ui.plot_panel.plot.draw_plot(Time, Value_I, Value_Q, Value)

def NLNF(): #НЛЧМ

    if ui.left_panel.nlchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "NLNF"
    plotb()

def LNF(): #ЛЧМ

    if ui.left_panel.lchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "LNF"
    plotb()

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

    amplify = ui.left_panel.ku_spinbox.value()
    radio.configure(amplify = amplify)
    plotb()


app = QApplication(sys.argv)
ui = UI.DemoWindow()

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
ui.left_panel.radio_radiobutton.toggled.connect(plotb)
ui.left_panel.lchm_radiobutton.toggled.connect(LNF)
ui.left_panel.nlchm_radiobutton.toggled.connect(NLNF)
ui.button_panel.exit_button.clicked.connect(close)
ui.button_panel.plot_button.clicked.connect(plotb)

#Привязка изменения значения в спинбоксах
ui.left_panel.ku_spinbox.valueChanged.connect(redraw_plot_amplify)
ui.time_panel.time_stop_spinbox.valueChanged.connect(redraw_plot_stop)
ui.time_panel.time_start_spinbox.valueChanged.connect(redraw_plot_start)

radio = Radiopulse(amplify = ui.left_panel.ku_spinbox.value())
radio_mod = SignalCl() 
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
