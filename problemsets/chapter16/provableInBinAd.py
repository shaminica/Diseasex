import utils
from binAd import isProof


def provableInBinAd(inString, maxString=1000):
    proofString = ''
    i =0

    while True:
        try:
            res = isProof(proofString, inString)
        except:
            res = 'no'

        if res == 'yes':
            return res

        proofString = utils.nextASCII(proofString)
        i += 1

        if i == maxString:
            return 'Maximum reached'
