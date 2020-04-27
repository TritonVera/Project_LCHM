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
f = 0
w0 = 0

#Отклонение по частоте
deltaF = 0
deltaW_N = 0
deltaW_L = 0

#Параметры импульса
imp = 0
space = 0

class SignalCl:

    def __init__(self):
        
        self.type_of_signal = "LNF"
        self.Configure_values()
        self.Configure_time()
    
    def Setup_par(self,F,Imp,T):
        global f, w0, deltaF, deltaW_N, deltaW_L, imp, space

        f = F
        w0 = 2*pi*f
        
        deltaF = 2*f
        deltaW_N = 2*pi*deltaF
        deltaW_L = 2*pi*deltaF

        imp = Imp*Mult
        space = (T-Imp)*Mult
        
        return(0)
        
   
    def Configure_time(self, Start = None, Stop = None):
        
        self.Start = 0
        self.time = 1000
        if Start != None and Stop != None:
            self.Start = Start*Mult
            self.time = Stop - Start
        self.dots_per_osc = 100
        self.dots = int(self.time*Mult*(f+deltaF)*self.dots_per_osc)
        
        self.Par = self.Gen_Signal(self.dots, self.dots_per_osc, self.Start)
        
        self.Time = self.Par[0]
        self.Signal = self.Par[1]
        self.I = self.Par[2]
        self.Q = self.Par[3]
        
        
        return(0)
        
    def Configure_values(self, Amplify_I = 1, Amplify_Q = 1, F = 0.1, Imp = 100, T = 125):
        
        self.Amplify_I = Amplify_I
        self.Amplify_Q = Amplify_Q
        
        self.Setup_par(F*10**6, Imp, T)
        
        return(0)

    def Gen_Signal(self, N, N_per_osc, Start):
        
        Time = [0]*N
        Signal = [0]*N
        I = [0]*N
        Q = [0]*N
        
        Signals = {'LNF':self.LNF,'NLNF':self.NLNF}
        T = imp + space
        
        for i in range(0,N):
            now = i/(N_per_osc*(f+deltaF)) + space + Start
            K = int(now/T)
            
            Time[i] = (now - space)/Mult
            Signal[i], I[i], Q[i] = Signals[self.type_of_signal](now-K*T-space)
            
            if now >= T*K and now < T*K+space:
                Signal[i] = 0
                I[i] = 0
                Q[i] = 0
        
        return(Time, Signal, I, Q)
        
    def AutoGen(self, FPS = 50, Speed = 10):
        
        one_computation_add_time = Speed*Mult/FPS
        add_dots = int(one_computation_add_time*(f+deltaF)*self.dots_per_osc)
        add_per_osc = self.dots_per_osc
        
        if add_dots < 20:
            add_dots = 20
            add_per_osc = add_dots/(one_computation_add_time*(f+deltaF))
            
        self.Par = self.Gen_Signal(add_dots,add_per_osc,self.Time[-1]*Mult)
        
        self.Time.extend(self.Par[0])
        self.Signal.extend(self.Par[1])
        self.I.extend(self.Par[2])
        self.Q.extend(self.Par[3])

        
        if self.Time[-1]-self.Time[0] > self.time:
            compare = False
            while compare != True:
                del self.Time[0]
                del self.Signal[0]
                del self.I[0]
                del self.Q[0]
                if self.Time[-1]-self.Time[0] <= self.time:
                    compare = True
        
        return(0)

    def NLNF(self,i):

        A_I = A * self.Amplify_I
        A_Q = A * self.Amplify_Q
        fi0 = 0
#        F0 = 0
#        fi_t = (deltaW_N/Omega)*sin(Omega*i+F0)
        fi_t = (deltaW_N/imp**8)*i**9
        I = A_I*cos(fi_t+fi0)
        Q = A_Q*sin(fi_t+fi0)
        S = I*cos(w0*i)-Q*sin(w0*i)

        return(S,I,Q)

    def LNF(self,i):
        
        A_I = A * self.Amplify_I
        A_Q = A * self.Amplify_Q
        
        fi0 = 0
        fi_t = (deltaW_L/imp)*i**2
        I = A_I*cos(fi_t+fi0)
        Q = A_Q*sin(fi_t+fi0)
        S = I*cos(w0*i)-Q*sin(w0*i)

        return(S,I,Q)
        

        
