import json
from .systems import systems_mapping
from .systems.System import System

class CFGLoader(object):
    
    _jo:dict
    
    def __init__(self, fp):
        self._jo = json.load(fp)
    
    def getSys(self) -> System:
        return systems_mapping[self._jo["type"]](self._jo["setpoint_range"], self._jo["output"])
        