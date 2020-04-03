# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:00:12 2020

@author: Григорий
"""
from matplotlib import pyplot
from ExciterObj import Signal

Radio = Signal()
Radio.Configure(Start = 0,Stop = 100)
Time, Value = Radio.Gen_Signal(1,'LNF')

fig,(ax1) = pyplot.subplots(1,1,figsize = (5,5))
ax1.plot(Time,Value)


