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
            self.__amplify_i = 1
            self.__amplify_q = 1
            self.__start_time = 0
            self.__step_time = 1.0 / 360
            self.__end_time = 20
            self.__phase = 0

            # Создание дискретов времени
            self.xpoints = self.arange(start = self.__start_time, stop = self.__end_time)

            # Создание пустых массивов точек
            self.Ipoints = []      #Косинусоидальная квадратура сигнала
            self.Qpoints = []      #Синусоидальная квадратура сигнала
            self.Zpoints = []      #Комплексный сигнал
            self.test_points = []  # Тестируемый сигнал 

            for i in self.xpoints:
                self.gen_signal(i)

    #Конфигуратор сигнала
    def configure(self, length = None, period_pulse = None, number = None,
                  period_packet = None, frequency = None, amplify_i = None,
                  amplify_q = None, phase = None):
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
        if (amplify_i != None):
            self.__amplify_i = amplify_i
        if (amplify_q != None):
            self.__amplify_q = amplify_q
        if (phase != None):
            self.__phase = phase

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
        self.test_points = []

        for i in self.xpoints:
            self.gen_signal(i)
        
    #Функция генерирования массивов точек радиосигнала
    def gen_signal(self, in_time_c):
        #Алгоритм заполнения массивов
        if (in_time_c % self.__period_packet) > (self.__number * self.__period_pulse):
            self.Ipoints.append(0)
            self.Qpoints.append(0)
            self.test_points.append(0)
        else:
            if (in_time_c % self.__period_packet % self.__period_pulse) > self.__length:
                self.Ipoints.append(0)
                self.Qpoints.append(0)
                self.test_points.append(0)
            else:
                self.Ipoints.append(self.__amplify_i * math.cos(math.pi * self.__phase / 180))
                # self.Ipoints.append(math.cos(2 * math.pi * in_time_c / self.__period_pulse))
                self.Qpoints.append(self.__amplify_q * math.sin(math.pi * self.__phase / 180))
                # self.Qpoints.append(math.sin(2 * math.pi * in_time_c / self.__period_pulse))
                self.test_points.append(self.__amplify_i * self.__length / self.__period_pulse * 
                    (math.sin(2 * math.pi * math.pi * self.__length / self.__period_pulse) /
                             (2 * math.pi * math.pi * self.__length / self.__period_pulse)))

        self.Zpoints.append((self.Ipoints[-1] * self.garmonic(in_time_c, self.__frequency))
                            - (self.Qpoints[-1] * self.garmonic(in_time_c, self.__frequency)))

    #Функция гармонического сигнала
    def garmonic(self, tm, freq, amp = 1.0):
        signal = amp * math.cos(2 * math.pi * freq * tm)
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

    def auto(self, fps, speed = 10):
        for i in self.arange(self.__end_time + self.__step_time, 
                              self.__end_time + (speed/fps)):
            self.gen_signal(i)
            self.xpoints.append(i)
            self.xpoints.pop(0)
            self.Ipoints.pop(0)
            self.Qpoints.pop(0)
            self.Zpoints.pop(0)
            self.test_points.pop(0)

        self.__start_time = self.xpoints[0]
        self.__end_time = self.xpoints[-1]
