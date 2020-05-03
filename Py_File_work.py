# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:13:57 2020

@author: Григорий
"""

from ExciterObj import SignalCl

#handle = open("test.txt")
#handle = open(r"C:\Users\mike\py101book\data\test.txt", "r") 

#handle = open("test.txt", "r") #r - read mod
#data = handle.read() # read just one line  
#print(data)
#handle.close()

#handle = open("test.txt", "r")
#data = handle.readlines() # read ALL the lines!
#print(data)
#handle.close()

#handle = open("output.txt", "w") #w - write mod wb - write binary mod 
#handle.write("This is a test!")
#handle.close()

Radio = SignalCl()
Radio.Configure_values(F = 0.1, Imp = 100, T = 1000)
Radio.Configure_time(Start = 0, Stop = 1000)

Filer = open("title.txt","r")
title = Filer.readlines()
Filer.close()

File = open("LCHM.txt","w")
N = len(title)
for i in range(0,N):
    File.write(str(title[i]))
File.write("\n")    

N = len(Radio.Signal)
for i in range(0,N):
    File.write(str('{0:5.3f}'.format(Radio.Time[i]))+"E-006,")
    File.write(str('{0:5.3f}'.format(Radio.Signal[i]))+"\n")
File.close()
print("end")