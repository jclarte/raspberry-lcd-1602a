
import smbus

import time

DEVICE_BUS = 1
DEVICE_ADDR = 0x3f

DISPLAY_OFF = int("0b00001000", 2)
DISPLAY_ON = int("0b00001100", 2)

bus = smbus.SMBus(DEVICE_BUS)

# off/on/off on display with 5s pause
bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_OFF)
time.sleep(5)
bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_ON)
time.sleep(5)
bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_OFF)


