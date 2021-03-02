#!/usr/bin/env python3

import serial
import minimalmodbus
from time import sleep

client = minimalmodbus.Instrument('COM10', 1)  # port name, slave address (in decimal)
client.serial.baudrate = 115200  # baudrate
client.serial.bytesize = 8
client.serial.parity   = serial.PARITY_EVEN
client.serial.stopbits = 1
client.serial.timeout  = 0.1      # seconds
client.address         = 1        # this is the slave address number
client.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client.clear_buffers_before_each_transaction = True

#######################
# informations
# print(client)
print('RS-485 Configurations')
print('Port:\t\t', client.serial.port)
print('Baudrate:\t', client.serial.baudrate)
print('Byte Size:\t', client.serial.bytesize)
print('Parity:\t\t', client.serial.parity)
print('Stopbits:\t', client.serial.stopbits)
print('Timeout:\t', client.serial.timeout)
print()

while True:
    temperatures = client.read_registers(248, 4)  # Registernumber, number of decimals
    print("temperatures: ", temperatures)
    print()
    driver_temp  = client.read_register(248) # read 2bytes (16bit) 
    print("driver temp: ", driver_temp)
    driver_temp  = client.read_float(248)
    print("driver temp: ", driver_temp)
    driver_temp  = client.read_long(248) # read 4bytes (32bit)
    print("driver temp: ", driver_temp)
    sleep(1)