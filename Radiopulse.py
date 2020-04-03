import math

class Radiopulse():
	#Конструктор объекта
	def __init__(self, length = 2.0, period_pulse = 4.0, number = 10,\
				 period_packet = 100, frequency = 2, start_time = 0.1,\
				 step_time = 0.01, end_time = 99.0, amplify = 1):
            self.__length = length
            self.__period_pulse = period_pulse
            self.__number = number
            self.__period_packet = period_packet
            self.__frequency = frequency
            self.__amplify = amplify
            self.__start_time  = start_time
            self.__step_time = start_time
            self.__end_time  = end_time
            self.gen_signal()

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
		self.gen_signal()

	#Конфигуратор времени
	def time_configure(self, start_time = None, step_time = None, end_time = None):
		if (start_time != None):
			self.__start_time = start_time
		if (step_time != None):
			self.__step_time = step_time
		if (end_time != None):
			self.__end_time = end_time
		self.gen_signal()
		
	#Функция генерирования массивов точек радиосигнала
	def gen_signal(self):

		#Создание дискретов времени
		self.xpoints = self.arange(start = self.__start_time, stop = self.__end_time,
							  step = self.__step_time)

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
		r = 'Test'
		print("I am working\n But you NOOOOT, %s\n" % r)

	def arange(self, start, stop, step):
		rang = []
		point = start
		while (point < stop):
			rang.append(point)
			point += step
		return rang
