
def DD(Fvals, Funcvals):
    # n = input("Enter n")
    n = len(Fvals)
    F = [[0 for x in range(n)] for y in range(n)]
    ret = [0] * n

    # for x in range(0, n):
    #   val = input("Enter num: " + str(x))
    #  Fvals[x] = val
    # for x in range(0, n):
    #   val = input("Enter num: " + str(x))
    #  Funcvals[x] = val

    for i in range(0, n):
        F[i][0] = Funcvals[i]
    for i in range(1, n):
        for j in range(1, i+1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (Fvals[i] - Fvals[i - j])
    for i in range(0, n):
        ret[i] = F[i][i]
        #print 'a'+ str(i) + ': ' + str(F[i][i])
    return ret

if __name__ == "__main__":
    x = [0.9, 1.3, 1.9, 2.1, 2.6, 3, 3.9, 4.4, 4.7, 5, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12, 12.6, 13, 13.3]
    y = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5,
         0.4, 0.25]
    pr = DD(x, y)
    for i in range(0, len(x)):
        print 'a'+ str(i) + ': ' + str(pr[i])
