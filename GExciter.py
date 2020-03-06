#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:17 2020

@author: Григорий
@author: Ivan
"""

from Mimp import *


app = QApplication([])
ui = uic.loadUi("Exciter.ui")
type_of_signal = "test"

def close(): #Закрыть

    ui.close()

def plotb(): #Построить

    """Вставка функции для реализации пачки радиоимпульсов"""
    if ui.radioButton_3.isChecked() == True:
        radio = Radiopulse(amplify = ui.doubleSpinBox.value())
        m.plot(radio.xpoints_sec, radio.Ipoints)
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


#Привязка кнопок
ui.pushButton.clicked.connect(close)
ui.pushButton_2.clicked.connect(plotb)
ui.radioButton.toggled.connect(LNF)
ui.radioButton_2.toggled.connect(NLNF)

#Создание виджета графика
m = PlotCanvas(ui,4,3,100)
a = ui.width()
m.move(0.5*a,0)

ui.show()
exit(app.exec_())
