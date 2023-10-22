import itertools
import random
from time import sleep

import numpy as np

# if __name__ == '__main__':
# B = range(1, 61)
# H = range(1, 61)
# d_H = np.single(np.arange(0.0, 1.1, 0.1))
# d = list(sorted(set([float('{:.2f}'.format(i * j)) for i, j in itertools.product(H, d_H)])))
# T = range(1, 41)
# q = range(0, 51, 5)
# wq = range(1, 16)
# xq = range(1, 16)
# R_int = [0.6, 0.7, 0.8, 0.9, 1.0]
# gamma = range(14, 23, 1)
# s_u_ref_top = [1]
# s_u_ref_top.append(list(range(5, 41, 5)))
# s_u_inc = list(np.single(np.arange(1.25, 4, 0.25)))
# s_u_txc = list(np.single(np.arange(0.55, 1.05, 0.05)))
# s_u_dss = list(np.single(np.arange(0.55, 1.05, 0.05)))
# print(len([i for i in
#            itertools.product(B, H, d, T, q, wq, xq, R_int, gamma, s_u_dss, s_u_txc, s_u_inc, s_u_ref_top)]))

# H = range(2, 21, 2)
# B_H = np.single(np.arange(0.5, 5.5, 0.5))
# B = list(sorted(set([float('{:.2f}'.format(i * j)) for i, j in itertools.product(H, B_H)])))
# q = range(0, 51, 5)
# R_int = [0.6, 0.7, 0.8, 0.9, 1.0]
# gamma = range(14, 21, 1)
# s_u = range(25, 250, 25)
# print(len([i for i in
#            itertools.product(B, H, q, R_int, gamma, s_u)]))

# H = range(2, 13, 2)
# B = range(2, 13, 2)
# # B_H = list(sorted(list([float('{:.2f}'.format(i / j)) for i, j in itertools.product(B, H)])))
# q = range(0, 51, 10)
# R_int = [0.6, 0.8, 1.0]
# gamma = range(14, 21, 1)
# s_u = [25, 50, 75, 100, 150]
# print(len([i for i in
#            itertools.product(B, H, q, R_int, gamma, s_u)]))

from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support


def func(a, b):
    return a + b


def main():
    a_args = [1]
    second_arg = 1
    with Pool() as pool:
        L = pool.starmap(func, [(1, 1)])
        M = pool.starmap(func, zip(a_args, repeat(second_arg)))
        N = pool.map(partial(func, b=second_arg), a_args)
        print(L, M, N)
        assert L == M == N


if __name__ == "__main__":
    freeze_support()
    main()
