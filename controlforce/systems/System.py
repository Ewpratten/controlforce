class System(object):
    
    setpoint_range:list
    outupt:dict
    
    def __init__(self, setpoint_range:list, output:dict)->None:
        self.setpoint_range = setpoint_range
        self.outupt = output