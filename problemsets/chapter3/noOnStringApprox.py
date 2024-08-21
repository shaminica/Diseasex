import utils; from utils import rf
from containsGAGA import *
from longerThan1K import *
from maybeLoop import *
from yes import *
def noOnStringApprox(progString, inString):   
    if progString == rf('containsGAGA.py'):
        return 'yes' if containsGAGA(inString) == 'no' else 'no'
    elif progString == rf('longerThan1K.py'):
        return 'yes' if longerThan1K(inString) == 'no' else 'no'
    elif progString == rf('yes.py'):
        return 'yes' if yes(inString) == 'no' else 'no'
    elif progString == rf('maybeLoop.py'):
        if not 'secret sauce' in inString: 
            return 'no'
        else:
            return 'yes' if maybeLoop(inString) == 'no' else 'no'
    else:
        return 'unknown' 
