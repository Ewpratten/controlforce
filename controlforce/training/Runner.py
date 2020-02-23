import random
from ..systems.System import System
from ..systems.PIDController import PIDState

class Runner(object):
    setpoint:float
    sys:System
    state:PIDState
    
    def __init__(self, sys:System, KP_R,KI_R,KD_R):
        # Get a random setpoint to run
        self.setpoint =  
        
        self.sys = sys
        
        self.state = PIDState()
        
        # Config state
        self.state.period = sys.output["period"]
        self.state.KP = random.choice(KP_R)
        self.state.KI = random.choice(KI_R)
        self.state.KD = random.choice(KD_R)
        
    def update(self):
        pass
    
    def getStabilityRanking(self) -> float:
        pass
        