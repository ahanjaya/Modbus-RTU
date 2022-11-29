# MODBUS RTU [RS-485]

This is example code to run modbus RTU using python with minimalmodbus or pymodbus libraries

## Installation
```
conda create -n modbus_env python=3.7 pip
pip install -r requirement.txt
```

### Packages (requirement.txt)
```
pyserial
minimialmobdus
pymodbus
numpy
```

## Run the code
1. Using minimalmodbus library
```
python modbus_min.py
```

2. Using pymodbus library
```
python modbus_py.py
```

## References
1. https://minimalmodbus.readthedocs.io/en/stable/usage.html
2. https://minimalmodbus.readthedocs.io/en/stable/apiminimalmodbus.html
3. https://stackoverflow.com/questions/60431210/modbus-rtu-master-python-script-with-minimalmodbus
