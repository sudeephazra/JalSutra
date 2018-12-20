
MESSAGE_TIMESPAN = 2000
SIMULATED_DATA = False
I2C_ADDRESS = 0x77

# Channels
CHANNEL_TEMPERATURE_HUMIDITY = 17
CHANNEL_SOIL_MOISTURE = 26 # HIGH = sufficient moisture, LOW = low moisture
CHANNEL_RAIN_SENSOR = 22 # HIGH = no rain, LOW = rain detected
CHANNEL_WATER_PUMP = 13
CHANNEL_DRAINAGE = 19

# Soil Moisture Sensor Settings
SOIL_MOISTURE_DRY = 5 # Reading from moisture sensor in air
SOIL_MOISTURE_WET = 1 # Reading from moisture sensor in water
SOIL_MOISTURE_WARNING = 30