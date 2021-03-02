#!/usr/bin/env python3

import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

client = ModbusClient(method='rtu', port="COM10", baudrate=115200, parity='E', timeout=0.1)
connection = client.connect()

read_vals  = client.read_holding_registers(248, 10, unit=1) # start_address, count, slave_id
print(read_vals.registers)

# write registers
# write  = client.write_register(1,425,unit=1)# address = 1, value to set = 425, slave ID = 1