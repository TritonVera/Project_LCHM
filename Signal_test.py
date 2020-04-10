# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:00:12 2020

@author: Григорий
"""
from matplotlib import pyplot
from ExciterObj import SignalCl

Radio = SignalCl()
Radio.Configure(Start = 0,Stop = 300)
Time, Value, Value_I, Value_Q = Radio.Gen_Signal(2,'LNF')

fig,(ax1,ax2) = pyplot.subplots(2,1,figsize = (10,10))
ax1.plot(Time,Value)
ax2.plot(Time,Value_I)
ax2.plot(Time,Value_Q)


