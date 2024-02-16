# Modbus Client
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder


print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
reg = 0; address = 0

# writing to coils and reading input discrete inputs
client.write_coil(1, True) #writing to the 1st coil address true value and than reading it
client.write_coil(2, False) #writing to the 1st coil address true value and than reading it
result = client.read_coils(1,2)
print(f'the coils response are: {result.bits[0], result.bits[1]}')

# initialize data
data = [0.1, 1.1, 2.1, 3.1, 4.1]
