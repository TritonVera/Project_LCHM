# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:00:12 2020

@author: Григорий
"""
from matplotlib import pyplot
import sys
sys.path.append("C:\\Users\\Григорий\\Desktop\\CodeBox\\RepBox\\Project_LCHM")
from ExciterObj import SignalCl

Radio = SignalCl()
Radio.type_of_signal = "NLNF"
Radio.Configure_values(F = 0.1, Imp = 100, T = 1000)
Radio.Configure_time(Start = 0, Stop = 100)
#Radio.type_of_signal = "LNF"
#Radio.Configure_time(Start = 0,Stop = 100)

fig,(ax1,ax2,ax3) = pyplot.subplots(3,1,figsize = (10,15))
ax1.plot(Radio.Time,Radio.Signal)
ax2.plot(Radio.Time,Radio.I)
ax2.plot(Radio.Time,Radio.Q)
ax3.plot(Radio.Time,Radio.Wt)

#for i in range(0,3):
#    Radio.Configure_values(Amplify_I = 1,Amplify_Q = 1,F = 0.5)
#    Radio.AutoGen(1,50)
    
#    fig,(ax1,ax2) = pyplot.subplots(2,1,figsize = (10,10))
#    ax1.plot(Radio.Time,Radio.Signal)
#    ax2.plot(Radio.Time,Radio.I)
#    ax2.plot(Radio.Time,Radio.Q)