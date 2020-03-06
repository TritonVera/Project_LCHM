#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:28:34 2020

@author: Григорий
"""
from matplotlib import pyplot
from math import cos,sin,pi

A = 1
f = 400000
deltaF = 0.5*f
Omega = 2*pi*20000
NT = 2

w0 = 2*pi*f
deltaW = 2*pi*deltaF
F0 = 0
fi0 = 0
imp = 100*10**-6
k = deltaW/imp
dopt = 0.01*10**-3
dop = round(dopt*(f+deltaW)*100)

N = round(imp*(f+deltaW)*100)
S = [0]*(N+dop)
T = [i*(imp+dopt)/(N+dop) for i in range (0,N+dop)]

Sign = [0]*len(S)*NT
Time = [i*(imp+dopt)/(N+dop) for i in range(0,(N+dop)*NT)]


class SignalObj:

    def __init__(self,tf):

        self.tofs = tf
        self.signal_Tlen(N,dop)
        self.signal()


    def NLNF(self,i): #НЛЧМ

        fi_t = (deltaW/Omega)*sin(Omega*i+F0)+fi0
        I = A*cos(fi_t)
        Q = A*sin(fi_t)
        S = I*cos(w0*i)-Q*sin(w0*i)

        return(S)

    def LNF(self,i): #ЛЧМ

        w = k*i+w0
        S =A*cos(w*i+fi0)

        return(S)

    def signal_Tlen(self,Ns,dops): #Заполнение периода значений сигнала

        for i in range (0,Ns+dops):

            if i<Ns:
                if self.tofs == "NLNF":
                    S[i] = self.NLNF(imp*i/N)
                if self.tofs == "LNF":
                    S[i] = self.LNF(imp*i/N)
            else:
                S[i] = 0

        return(0)

    def signal(self): #Заполнение значений всего сигнала

        for i in range(1,NT+1):
            for j in range(0,N+dop):
                Sign[j] = S[j]
                if (i>1) :
                    Sign[j+(i-1)*(N+dop)] = S[j]

        return(0)

    def UM(self,KU): #Умножение на коэффициент усилиния

        for i in range(0,len(S)*NT):
            Sign[i] = Sign[i]*KU

        return(0)

