import utils
from binAd import isProof


def provableInBinAd(inString):
    proofString = ''

    while True:
        try:
            res = isProof(proofString, inString)
        except:
            res = False

        if res:
            return 'yes'

        proofString = utils.nextASCII(proofString)
