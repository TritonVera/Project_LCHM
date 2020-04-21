import math
import time

class Radiopulse():
    #Конструктор объекта
    def __init__(self):
            self.__length = 2.0
            self.__period_pulse = 4.0
            self.__number = 10
            self.__period_packet = 100
            self.__frequency = 2
            self.__amplify = 1
            self.__start_time  = 0
            self.__step_time = 1.0 / (self.__frequency * 36)
            self.__end_time  = 100

            # Создание дискретов времени
            self.xpoints = self.arange(start = self.__start_time, stop = self.__end_time)

            # Создание пустых массивов точек
            self.Ipoints = []      #Косинусоидальная квадратура сигнала
            self.Qpoints = []      #Синусоидальная квадратура сигнала
            self.Zpoints = []      #Комплексный сигнал

            for i in self.xpoints:
                self.gen_signal(i)

    #Конфигуратор сигнала
    def configure(self, length = None, period_pulse = None,
                  number = None, period_packet = None,
                  frequency = None, amplify = None):
        if (length != None):
            self.__length = length
        if (period_pulse != None):
            self.__period_pulse = period_pulse
        if (number != None):
            self.__number = number
        if (period_packet != None):
            self.__period_packet = period_packet
        if (frequency != None):
            self.__frequency = frequency
        if (amplify != None):
            self.__amplify = amplify

    #Конфигуратор времени
    def time_configure(self, start_time = None, end_time = None):
        if (start_time != None):
            self.__start_time = start_time
        
        if (end_time != None):
            self.__end_time = end_time
        
        # Создание дискретов времени
        self.xpoints = self.arange(start = self.__start_time, stop = self.__end_time)

        # Переинициализация точек
        self.Ipoints = []
        self.Qpoints = []
        self.Zpoints = []

        for i in self.xpoints:
            self.gen_signal(i)
        
    #Функция генерирования массивов точек радиосигнала
    def gen_signal(self, in_time_c):
        #Алгоритм заполнения массивов
        while in_time_c > self.__period_packet:
            in_time_c = in_time_c - self.__period_packet
        if in_time_c > (self.__number * self.__period_pulse):
            self.Ipoints.append(0)
            self.Qpoints.append(0)
            self.Zpoints.append(0)
        else:
            while in_time_c > self.__period_pulse:
                in_time_c = in_time_c - self.__period_pulse
            if in_time_c > self.__length:
                self.Ipoints.append(0)
                self.Qpoints.append(0)
                self.Zpoints.append(0)
            else:
                self.Ipoints.append(self.garmonic(in_time_c, self.__frequency,
                                    self.__amplify))
                self.Qpoints.append(self.garmonic(in_time_c, self.__frequency,
                                    self.__amplify, phs = math.pi/2))
                self.Zpoints.append(self.Ipoints[-1] - self.Qpoints[-1])

    #Функция гармонического сигнала
    def garmonic(self, tm, freq, amp = 1.0, phs = 0.0):
        signal = amp * math.sin((2 * math.pi * freq * tm) + phs)
        return signal

    def send_test(self):
        r = 'Test'
        print("I am working\n But you NOOOOT, %s\n" % r)

    def arange(self, start, stop):
        rang = []
        point = start
        while (point < stop):
            rang.append(point)
            point += self.__step_time
        return rang

    def auto(self, length = None, period_pulse = None,
                  number = None, period_packet = None,
                  frequency = None, amplify = None, speed = 10):
        fps = 30
        self.configure(length, period_pulse, number, period_packet, frequency, amplify)
        print(self.arange(self.__end_time + self.__step_time, 
                             self.__end_time + (speed/fps)))
        for i in self.arange(self.__end_time + self.__step_time, 
                             self.__end_time + (speed/fps)):
            self.gen_signal(i)
            self.Ipoints.pop(0)
            self.Qpoints.pop(0)
            self.Zpoints.pop(0)

        self.__start_time = self.__start_time + (speed/fps)
        self.__end_time = self.__end_time + (speed/fps)
        self.xpoints = self.arange(start = self.__start_time, stop = self.__end_time)



