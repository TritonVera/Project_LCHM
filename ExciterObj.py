#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:28:34 2020

@author: Григорий
"""
from math import cos,sin,pi

#Предполагаем входное время со следующим множителем:
Mult = 10**-6

#Параметры несущей
A = 1
f = 200000*0.5
w0 = 2*pi*f

#Отклонение по частоте
deltaF = 2*f
deltaW_N = 2*pi*deltaF
deltaW_L = 2*pi*deltaF

#Параметры импульса
imp = 100*Mult
space = 25*Mult

class SignalCl:

    def __init__(self):
        
        self.Configure()

        
    def Configure(self, Start = 0, Stop = 100):
        
        self.Start = Start*Mult
        self.time = Stop - Start
        self.dots_per_osc = 100

        self.Signal = [0]*int(self.time*Mult*(f+deltaF)*self.dots_per_osc)
        self.I = [0]*len(self.Signal)
        self.Q = [0]*len(self.Signal)
        self.Time = [0]*len(self.Signal)
        
        return(0)

    def Gen_Signal(self,Amplify,type_of_signal):
        
        self.Amplify = Amplify
        Signals = {'LNF':self.LNF,'NLNF':self.NLNF}
        T = imp + space
        
        for i in range(0,len(self.Time)):
            now = i/(self.dots_per_osc*(f+deltaF)) + space + self.Start
            K = int(now/T)
            
            self.Time[i] = (now - space)/Mult
            self.Signal[i], self.I[i], self.Q[i] = Signals[type_of_signal](now-K*T-space)
            
            if now >= T*K and now < T*K+space:
                self.Signal[i] = 0
                self.I[i] = 0
                self.Q[i] = 0
            
            self.Signal[i] = self.Signal[i]*self.Amplify
            self.I[i] = self.I[i]*self.Amplify
            self.Q[i] = self.Q[i]*self.Amplify
        
        return(self.Time, self.Signal, self.I, self.Q)

    def NLNF(self,i):

       
        fi0 = 0
#        F0 = 0
#        fi_t = (deltaW_N/Omega)*sin(Omega*i+F0)
        fi_t = (deltaW_N/imp**8)*i**9
        I = A*cos(fi_t+fi0)
        Q = A*sin(fi_t+fi0)
        S = I*cos(w0*i)-Q*sin(w0*i)

        return(S,I,Q)

    def LNF(self,i):
        
        fi0 = 0
        fi_t = (deltaW_L/imp)*i**2
        I = A*cos(fi_t+fi0)
        Q = A*sin(fi_t+fi0)
        S = I*cos(w0*i)-Q*sin(w0*i)

        return(S,I,Q)
        

        
