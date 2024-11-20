from typing import Any


class SmartDevice:
    device_count = 0
    def __init__(self, device_name, model_number, is_online=False) -> None:
        self.device_name = device_name
        self.model_number = model_number
        self.status = {}
        SmartDevice.device_count+=1
        self.is_online = is_online
        self.device_info = lambda: {"name": self.device_name, "model": self.model_number}
    
    def update_status(self, fet, val):
        self.status[fet]=val
    
    def get_status(self, fet):
        try:
            status= self.status[fet]
            return status
        except KeyError as exp:
            return 'Attribute not found'
        except Exception as exp:
            print(exp)
            
    def toggle_online(self):
        self.is_online = not self.is_online
        return self.is_online

    def reset(self):
        self.status = {}
        self.is_online = False
        SmartDevice.device_count=3
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        ret = f'{self.device_name} (Model: {self.model_number})'
        return ret
    
    @classmethod
    def reset_device_count(cls):
        cls.device_count = 0
    
