import argparse
from threading import Thread
import utils
import numpy as np


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--inString',
                        '-i',
                        type=str,
                        help=' factorization target')
    parser.add_argument('--K', '-K', type=int, help='number of threading')

    return parser.parse_args()


def factor_opt(M, search_range, nonDetSolution):

    for i in search_range:
        if M % i == 0:
            nonDetSolution.setSolution(str(i))


def main(args):

    M = int(args.inString)
    M_prime = int(np.sqrt(M))
    search_range = np.array([i + 2 for i in range(M_prime - 2)])

    splitted = np.array_split(search_range, args.K)

    ndSoln = utils.NonDetSolution()
    threads = []

    for split_range in splitted:
        t = Thread(target=factor_opt, args=(M, split_range, ndSoln))
        threads.append(t)

    res = utils.waitForOnePosOrAllNeg(threads, ndSoln)

    return res


if __name__ == '__main__':

    arg = get_arguments()
    res = main(arg)
    print(res)
