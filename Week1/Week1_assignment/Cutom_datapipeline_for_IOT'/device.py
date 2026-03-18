##############################
#Filename: device.py
#Date of Code: 10th March 2026
#Author: Praful Sharma
##############################

class IoTDevice: 
    def __init__(self, deviceId, location, data) -> None: 
        self.deviceId = deviceId
        self.location = location 
        self.data = data
        
    def info_dict(self) -> dict: # Dictionary
        return {
            self.__class__.__name__: "type", 
            self.deviceId: "deviceId",
            self.location: "location", 
            self.data: "data"
        }
        
class TemperatureSensor(IoTDevice): 
    pass 

class HumiditySensor(IoTDevice): 
    pass 

class MotionSensor(IoTDevice): 
    pass