from utils import DESS
from universal import universal

def repeat(inString):
    (progString, newInString) = DESS(inString)
    val = universal(progString, newInString)
    return val * 2