import time
import sys
import RPi.GPIO as GPIO
import Config

class Actuator:
	
	_WATER_PUMP_PORT = Config.CHANNEL_WATER_PUMP
	
	def __init__(self, WATER_PUMP_PORT=None):
		
		if WATER_PUMP_PORT is None:
			self.WATER_PUMP_PORT = _WATER_PUMP_PORT
		else:
			self.WATER_PUMP_PORT = WATER_PUMP_PORT
			
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.WATER_PUMP_PORT, GPIO.OUT)

		
	def pullup_port(self):
		GPIO.output(self.WATER_PUMP_PORT, GPIO.HIGH)


	def pulldown_port(self):
		GPIO.output(self.WATER_PUMP_PORT, GPIO.LOW)

		
	def cleanup(self):
		GPIO.cleanup(self.WATER_PUMP_PORT)
