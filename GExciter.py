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
from ExciterObj import *                #TODO(Григорий): Make refactoring

type_of_signal = "test"

def close(): #Закрыть

    sys.exit(app.exec_())

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""

    if ui.radio_radiobutton.isChecked():
        #radio.send_test()
        ui.plot.draw_plot(radio.xpoints, radio.Ipoints)
    else:
        n = SignalObj(type_of_signal) #Заполнение массивов времени и значения сигнала
        KU = ui.ku_spinbox.value()
        n.UM(KU) #Умножение значений на коэффициент усиления
        ui.plot.draw_plot(Time, Sign) #Построение графика

def NLNF(): #НЛЧМ

    if ui.nlchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "NLNF"
    plotb()

def LNF(): #ЛЧМ

    if ui.lchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "LNF"
    plotb()

def redraw_plot_start():

    start = ui.time_start_spinbox.value()
    stop = ui.time_stop_spinbox.value()
    if (stop < start):
        ui.time_stop_spinbox.setValue(ui.time_start_spinbox.value() + 1)
    radio.time_configure(start_time = start, end_time = stop)
    plotb()


def redraw_plot_stop():

    start = ui.time_start_spinbox.value()
    stop = ui.time_stop_spinbox.value()
    if (stop < start):
        ui.time_start_spinbox.setValue(ui.time_stop_spinbox.value() - 1)
    radio.time_configure(start_time = start, end_time = stop)
    plotb()


def redraw_plot_amplify():

    amplify = ui.ku_spinbox.value()
    radio.configure(amplify = amplify)
    plotb()


app = QApplication(sys.argv)
ui = UI.DemoWindow()

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
ui.radio_radiobutton.toggled.connect(plotb)
ui.lchm_radiobutton.toggled.connect(LNF)
ui.nlchm_radiobutton.toggled.connect(NLNF)
ui.exit_button.clicked.connect(close)

#Привязка изменения значения в спинбоксах
ui.ku_spinbox.valueChanged.connect(redraw_plot_amplify)
ui.time_stop_spinbox.valueChanged.connect(redraw_plot_stop)
ui.time_start_spinbox.valueChanged.connect(redraw_plot_start)

radio = Radiopulse(amplify = ui.ku_spinbox.value())
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
