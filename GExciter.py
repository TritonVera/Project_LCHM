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

    ui.close()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""
    if ui.radio_radiobutton.isChecked() == True:
        radio = Radiopulse(amplify = ui.ku_spinbox.value())
        #radio.send_test()
        ui.plot.draw_plot(radio.xpoints, radio.Ipoints)
        return
    """Конец вставки"""

    n = SignalObj(type_of_signal) #Заполнение массивов времени и значения сигнала
    #KU = ui.doubleSpinBox.value()
    #n.UM(KU) #Умножение значений на коэффициент усиления
    m.plot() #Построение графика

def NLNF(): #НЛЧМ

    if ui.nlchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "NLNF"

def LNF(): #ЛЧМ

    if ui.lchm_radiobutton.isChecked() == True:
        global type_of_signal
        type_of_signal = "LNF"

app = QApplication(sys.argv)
ui = UI.DemoWindow()

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
ui.ku_spinbox.valueChanged.connect(plotb)
ui.radio_radiobutton.toggled.connect(plotb)
#ui.lchm_radioButton.toggled.connect(LNF)
#ui.nlchm_radioButton.toggled.connect(NLNF)

""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
