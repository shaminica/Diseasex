from utils import WcbcException

def fird(inString):
    split = inString.split()

    if len(split) != 3:
        raise WcbcException("input must be composed of 3 numbers")

    M, a, b = int(split[0]), int(split[1]), int(split[2])
    
    if a > b:
        raise WcbcException("a must be equal to or smaller than b")
    
    for i in range(a, b + 1):
        if M % i == 0:
            return "yes"
    
    return "no"