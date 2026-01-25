import argparse
import numpy as np

import utils
import os
import time
import sys
from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--inString',
                        '-i',
                        type=str,
                        help=' factorization target')
    parser.add_argument('--K', '-K', type=int, help='Number of process')

    return parser.parse_args()


def factor_opt(M, search_range):

    for i in search_range:
        if M % i == 0:
            return str(i)
    return 'no'



def main(args):

    M = int(args.inString)
    M_prime = int(np.sqrt(M))
    search_range = np.array([i + 2 for i in range(M_prime - 2)])
    splitted = np.array_split(search_range, args.K)

    res = 'no'

    with ProcessPoolExecutor() as e:
        futures = set([e.submit(factor_opt, M, split_range)
                   for split_range in splitted])


        for future in as_completed(futures):
            temp = future.result()
            if temp !='no':
                res = temp

                return res

        # すべてnoだった場合はこちらを返す
        return res


if __name__ == '__main__':

    arg = get_arguments()
    res = main(arg)
    print(res)
