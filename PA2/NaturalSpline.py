

import matplotlib
matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
#import numpy as np
#import math


def NS(F,Fvals):
    # n = input("Enter numbers of x\'s: ")
    n = len(F)
    # F = [0] * (n)
    # Fvals = [0] * (n)

    h = [0] * n
    a = [0] * n
    l = [0] * n
    u = [0] * n
    z = [0] * n
    c = [0] * n
    b = [0] * n
    d = [0] * n
    # for x in range(0, n):
    # F[x] = input("Enter num " + str(x+1) + ": ")
    # for x in range(0, n):
    # Fvals[x] = input("Enter f(x" + str(x+1) + ")" + ": ")
    for x in range(0, n - 1):
        h[x] = F[x + 1] - F[x]
    for x in range(1, n - 1):
        a[x] = ((3 / h[x]) * (Fvals[x + 1] - Fvals[x])) - ((3 / h[x - 1]) * (Fvals[x] - Fvals[x - 1]))
    l[0] = 1
    for x in range(1, n - 1):
        l[x] = (2 * (F[x + 1] - F[x - 1])) - (h[x - 1] * u[x - 1])
        u[x] = (h[x]) / (l[x])
        z[x] = ((a[x]) - (h[x - 1] * z[x - 1])) / l[x]
    for x in range(n - 2, -1, -1):
        c[x] = z[x] - (u[x] * c[x + 1])
        b[x] = ((Fvals[x + 1] - Fvals[x]) / (h[x])) - (h[x] * (c[x + 1] + (2 * c[x])) / 3)
        d[x] = (c[x + 1] - c[x]) / (3 * h[x])


    return Fvals, b, c, d


if __name__ == "__main__":
    F = [0.9, 1.3, 1.9, 2.1, 2.6, 3, 3.9, 4.4, 4.7, 5, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12, 12.6, 13, 13.3]
    Fvals = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4,
             0.25]
    v,m,f,g = NS(F,Fvals)
    print "{:^25}   {:^25}   {:^25}   {:^25}".format("A", "B", "C", "D")
    print "{:-^110}".format("-")
    for i in range(0,len(Fvals)):
        print('{:^25s} | {:^25s} | {:^25s} | {:^25s}'.format(str(v[i]), str(m[i]), str(f[i]), str(g[i])))

