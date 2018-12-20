
import random
import time
import sys
import RPi.GPIO as GPIO
import re
from telemetry import Telemetry
import Adafruit_DHT
import Config

class SensorReader:
	
	_CHANNEL_TEMPERATURE_HUMIDITY = Config.CHANNEL_TEMPERATURE_HUMIDITY
	_CHANNEL_SOIL_MOISTURE = Config.CHANNEL_SOIL_MOISTURE
	_CHANNEL_RAIN_SENSOR = Config.CHANNEL_RAIN_SENSOR
	_temperature_humidity_sensor = Adafruit_DHT.DHT11
	
	def __init__(self, CHANNEL_TEMPERATURE_HUMIDITY=None, CHANNEL_SOIL_MOISTURE=None, CHANNEL_RAIN_SENSOR=None):
		
		if CHANNEL_TEMPERATURE_HUMIDITY is None:
			self.CHANNEL_TEMPERATURE_HUMIDITY = _CHANNEL_TEMPERATURE_HUMIDITY
		
		if CHANNEL_SOIL_MOISTURE is None:
			self.CHANNEL_SOIL_MOISTURE = _CHANNEL_SOIL_MOISTURE
		
		if CHANNEL_RAIN_SENSOR is None:
			self.CHANNEL_RAIN_SENSOR = _CHANNEL_RAIN_SENSOR
			
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.CHANNEL_TEMPERATURE_HUMIDITY, GPIO.IN)
		GPIO.setup(self.CHANNEL_SOIL_MOISTURE, GPIO.IN)
		GPIO.setup(self.CHANNEL_RAIN_SENSOR, GPIO.IN)

		
	def read_temperature_humidity_sensor_data(self):
		humidity, temperature = Adafruit_DHT.read_retry(self._temperature_humidity_sensor, self.CHANNEL_TEMPERATURE_HUMIDITY)
		return humidity, temperature

		
	def read_soil_moisture_data(self):
		soilMoisture = GPIO.input(self.CHANNEL_SOIL_MOISTURE)
		return soilMoisture

		
	def read_rainfall_data(self):
		isRaining = GPIO.input(self.CHANNEL_RAIN_SENSOR)
		return isRaining

		
	def cleanup(self):
		GPIO.cleanup(self.CHANNEL_TEMPERATURE_HUMIDITY)		
		GPIO.cleanup(self.CHANNEL_SOIL_MOISTURE)		
		GPIO.cleanup(self.CHANNEL_RAIN_SENSOR)		
