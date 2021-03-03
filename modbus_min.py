#!/usr/bin/env python3

import serial
import minimalmodbus
from time import sleep

client1 = minimalmodbus.Instrument('COM9', 1, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 115200  # baudrate
client1.serial.bytesize = 8
client1.serial.parity   = serial.PARITY_EVEN
client1.serial.stopbits = 1
client1.serial.timeout  = 0.1      # seconds
client1.address         = 1        # this is the slave address number
client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True

#######################
# informations
# print(client1)
# print('RS-485 Configurations')
# print('Port:\t\t', client1.serial.port)
# print('Baudrate:\t', client1.serial.baudrate)
# print('Byte Size:\t', client1.serial.bytesize)
# print('Parity:\t\t', client1.serial.parity)
# print('Stopbits:\t', client1.serial.stopbits)
# print('Timeout:\t', client1.serial.timeout)
# print()

# while True:
    #################################
    ###### temperatures read example

    # temperatures = client1.read_registers(248, 4)  # Registernumber, number of decimals
    # print()
    # print("temperatures: ", temperatures)
    # # driver_temp  = client1.read_register(248) # read single register 2bytes (16bit) 
    # # print("driver temp: ", driver_temp)
    # driver_temp  = client1.read_register(249, 1) # read single register 2bytes (16bit), with 1 floating point
    # print("driver temp: ", driver_temp)
    # # driver_temp  = client1.read_float(248)
    # # print("driver temp: ", driver_temp)
    # driver_temp  = client1.read_long(248) # read 4bytes (32bit)
    # print("driver temp: ", driver_temp)
    # motor_temp  = client1.read_long(250) # read 4bytes (32bit)
    # print("motor temp: ", motor_temp)
    # sleep(1)


    # output_stats  = client1.read_register(127) # read single register 2bytes (16bit)
    # print("output stats: {0:016b}".format(output_stats))

    # input_stats  = client1.read_register(125) # read single register 2bytes (16bit)
    # print("input stats: {0:016b}".format(input_stats))
    # sleep(1)


# # writing to holding register
# # client1.write_register(int("0x007D", 0), int("0x0000", 0), 1)
# client1.write_register(125, 16, number_of_decimals=0, functioncode=6)
# input_stats  = client1.read_register(125) # read single register 2bytes (16bit)
# print("input stats: {0:016b}".format(input_stats))

# client1.write_register(125, 0, number_of_decimals=0, functioncode=6)
# client1.write_register(int("0x007D", 0), 24, functioncode=6)

# client1.write_register(int("0x007D", 0), 16, functioncode=6)
# write_register(registeraddress, value, number_of_decimals=0, functioncode=16, signed=False)

# a = int('0000000000011000',2)
# print(a)


#####################################################################################
'''
Temperature
'''
# driver_temp  = client1.read_long(248) # read 4bytes (32bit)
# print("driver temp: ", driver_temp)


#####################################################################################
'''
Z-Home Pos (High-speed return-to-home operation)
**ZHOME is assigned to bit 4 of the driver input command (007Dh) in initial setting.
(10000 in a binary number=0010h in a hexadecimal number)
'''
# client1.write_register(int("0x007D", 0), int("0x0010", 0), functioncode=6) # Z-Home ON


#####################################################################################
'''
Change Operating Speed to 5000hz
'''
# client1.write_registers(int("0x0480", 0), [int("0x0000", 0), int("0x1388", 0)]) # 5000 = 1388h
# client1.write_registers(int("0x0480", 0), [int("0x0000", 0), int("0x2710", 0)]) # 10000 = 2710h

#####################################################################################
'''
**FW-POS is assigned to bit 15 of the driver input command (007Dh) in initial setting.
(0100 0000 0000 0000 in a binary number=4000h in a hexadecimal number)
'''
# client1.write_register(int("0x007D", 0), int("0x4000", 0), functioncode=6)

#####################################################################################
''' 
**Stop
'''
client1.write_register(int("0x007D", 0), int("0x0000", 0), functioncode=6) # Stop


#####################
#### Read I/O Command
input_stats  = client1.read_register(125) # read single register 2bytes (16bit)
print("input stats: {0:016b}".format(input_stats))
output_stats  = client1.read_register(127) # read single register 2bytes (16bit)
print("output stats: {0:016b}".format(output_stats))

client1.close_port_after_each_call = True