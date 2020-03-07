#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:17 2020

@author: Григорий
@author: Ivan
"""
import sys                              #System function
import Mimp                             #User interface classes

from PyQt5.QtWidgets import QApplication
from Radiopulse import *
from ExciterObj import *                #TODO(Григорий): Make refactoring

type_of_signal = "test"

def close(): #Закрыть

    ui.close()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""
    if ui.radioButton_3.isChecked() == True:
        global m
        radio = Radiopulse(amplify = ui.doubleSpinBox.value())
        radio.send_test()
        del m
        m = MakePlot(ui.PlotWidget, 3, 3, 100, radio.xpoints, radio.Ipoints)
        m.move(0, 0)
        return
    """Конец вставки"""

    n = SignalObj(type_of_signal) #Заполнение массивов времени и значения сигнала
    KU = ui.doubleSpinBox.value()
    n.UM(KU) #Умножение значений на коэффициент усиления
    m.plot() #Построение графика

def NLNF(): #НЛЧМ

    if ui.radioButton_2.isChecked() == True:
        global type_of_signal
        type_of_signal = "NLNF"

def LNF(): #ЛЧМ

    if ui.radioButton.isChecked() == True:
        global type_of_signal
        type_of_signal = "LNF"

app = QApplication(sys.argv)
ui = Mimp.DemoWindow()

""" Реализация конструктора UI """
#ui = uic.loadUi("Exciter.ui")

#Привязка кнопок
#ui.pushButton.clicked.connect(close)
#ui.pushButton_2.clicked.connect(plotb)
#ui.radioButton.toggled.connect(LNF)
#ui.radioButton_2.toggled.connect(NLNF)

#Создание виджета графика
#m = PlotCanvas(ui.PlotWidget, 3, 3, 100)
#m.move(0, 0)
""" Конец реализации конструктора """

ui.show()
sys.exit(app.exec_())
