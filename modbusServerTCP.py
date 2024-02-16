# Modbus server (TCP)
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_async_server():
    nreg = 200
    # initializing data store with 200 available registers
    store = ModbusSlaveContext(di=ModbusSequentialDataBlock(0, [15]*nreg), 
                               co=ModbusSequentialDataBlock(0, [16]*nreg),
                               hr=ModbusSequentialDataBlock(0, [17]*nreg),
                               ir=ModbusSequentialDataBlock(0, [18]*nreg))
    # assigning the address bases of these registers
    context = ModbusServerContext(slaves=store, single=True)
    # initialize the server information
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'AppMonitor'
    identity.ProductCode = 'APM'
    identity.VendorUrl = 'https://appmonitor.com'
    identity.ProductName = 'Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '1.0.0' 

    try:
        StartTcpServer(context=context, host='localhost', identity=identity, \
                   address = (serverAddress,502))
        print("Server is online")
    except:
        print("Shutdown server...")
if __name__ == "__main__":
    # TCP Server
    serverAddress = "127.0.0.1"
    print(f'Modbus server started on port 502 and address {serverAddress}')
    run_async_server()