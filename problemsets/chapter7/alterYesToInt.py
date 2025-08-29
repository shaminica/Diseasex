from utils import DESS
from universal import universal

def alterYesToInt(inString):
    (progString, newInString) = DESS(inString)
    val = universal(progString, newInString)
    if val == 'yes':
        return '1'
    else:
        return 'This is not an integer.'