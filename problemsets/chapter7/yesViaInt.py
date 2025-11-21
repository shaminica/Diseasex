from intOnString import intOnString # oracle function
from utils import ESS, rf

def yesViaInt(progString, inString):
    singleString = ESS(progString, inString)
    return intOnString(rf('alterYesToInt.py'), singleString)