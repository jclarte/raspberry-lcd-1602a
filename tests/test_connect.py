
import smbus

import time

DEVICE_BUS = 1
DEVICE_ADDR = 0x3f

DISPLAY_OFF = 0x00
DISPLAY_ON = 0x0e
DISPLAY_CURSOR_ON = 0x0f

bus = smbus.SMBus(DEVICE_BUS)

# read register
for i in range(256):
    b = bus.read_byte_data(DEVICE_ADDR, i)
    print(f"{i:02x}:{b:02x}", end=" ")
    if i%16 == 15:
        print()


# off/on/off on display with 5s pause
print("Display OFF")
start_time = time.time()
while time.time() - start_time < 5:
    bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_OFF)
print(bus.read_byte_data(DEVICE_ADDR, 0x00))


print("Display ON")
start_time = time.time()
while time.time() - start_time < 5:
    bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_ON)
print(bus.read_byte_data(DEVICE_ADDR, 0x00))
time.sleep(5)

print("Display OFF")
start_time = time.time()
while time.time() - start_time < 5:
    bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_OFF)
print(bus.read_byte_data(DEVICE_ADDR, 0x00))

print("Display ON with cursor")
start_time = time.time()
while time.time() - start_time < 5:
    bus.write_byte_data(DEVICE_ADDR, 0x00, DISPLAY_CURSOR_ON)
print(bus.read_byte_data(DEVICE_ADDR, 0x00))

