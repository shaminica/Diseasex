from utils import DESS
from universal import universal

def applyBothTwice(inString):
    PQ, I = DESS(inString)
    P, Q = DESS(PQ)
    return universal(Q, universal(P, universal(Q, universal(P, I))))
