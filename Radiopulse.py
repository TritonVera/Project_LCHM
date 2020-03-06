import math

class Radiopulse():
	#Конструктор объекта
	def __init__(self, length = 2.0, period_pulse = 4.0, number = 10,\
				 period_packet = 100, frequency = 2, st = 0.0,\
				 stp = 0.001, nd = 99.0, amplify = 1):
		self.__length = length
		self.__period_pulse = period_pulse
		self.__number = number
		self.__period_packet = period_packet
		self.__frequency = frequency
		self.__amplify = amplify
		self.gen_signal(st, stp, nd)

	#Конфигуратор объекта
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

	#Функция генерирования массивов точек радиосигнала
	def gen_signal(self,start_time, step, end_time):
		#Инициализация внутренних переменных
		start_time_c = start_time
		step_c = step
		end_time_c = end_time

		#Создание дискретов времени
		self.xpoints = self.__time_step(start_time_c, step_c, end_time_c)
		self.xpoints_sec = self.to_seconds(self.xpoints)

		#Создание пустых массивов точек
		self.Ipoints = []		#Косинусоидальная квадратура сигнала
		self.Qpoints = []		#Синусоидальная квадратура сигнала
		self.Zpoints = []		#Комплексный сигнал

		#Алгоритм заполнения массивов
		for time_c in self.xpoints:
			in_time_c = time_c
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
		print("I am working")

	def __time_step(self, start, step, end):
		rang = []
		point = start
		rang.append(point)
		while point < end:
			point += step
			rang.append(point)
		return rang

	def to_seconds(self, lst):
		rang = []
		for point in range(0, len(lst)):
			rang.append(lst[point]/1000000)
		return rang
