from utils import DESS
from universal import universal

def recCrashOnString(inString):
    (progString, newInString) = DESS(inString)
    try:
        universal(progString, newInString)
    except:
        return 'yes'
    return 'no'