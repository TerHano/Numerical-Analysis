import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from DividedDifferences import DD
from NaturalSpline import NS

F = [0.9,1.3,1.9,2.1,2.6,3,3.9,4.4,4.7,5,6,7,8,9.2,10.5,11.3,11.6,12,12.6,13,13.3]
Func = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]
ret = DD(F,Func)
Fvals, b, c, d = NS(F,Func)
n = 21

for i in range(0,n-1):
    q = F[i]
    w = F[i+1]
    m = np.array(np.arange(q,w,.01))
    y = (Fvals[i] + (b[i]*(m-F[i])) + (c[i]*((m-F[i])**2)) + (d[i]*((m-F[i])**3)))
    plt.plot(m, y, 'r', label = 'Cubic Spline' if i == 0 else "")
plt.plot(F, Func, 'o', label = 'Given Points')

eq = str(ret[0]) + '+'
for c in range(1, n):
    eq += '(' + str(ret[c])
    for i in range(0, c):
        eq += '*(x-' + str(F[i]) + ')'
    eq += ')+'
eq = eq.rstrip('+')

DDx = []
DDy = []

for i in range(0,n-1):
    q = F[i]
    w = F[i + 1]
    m = np.array(np.arange(q, w, .01))
    for c in range(0,len(m)):
        num = eval(eq.replace('x', str(m[c])))
        DDx.append(m[c])
        DDy.append(num)
plt.plot(DDx,DDy,'g--', label = 'Divided Differences')
plt.title("Duck Lines")
plt.legend(loc='best')
plt.show()
