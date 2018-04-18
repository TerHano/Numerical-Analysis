from __future__ import division
import math


def parseEq(equation):
    equation = equation.replace('cos', 'math.cos')
    equation = equation.replace('sin', 'math.sin')
    equation = equation.replace('ln', 'math.log')
    equation = equation.replace('e', 'math.e')
    equation = equation.replace('tan', 'math.tan')
    equation = equation.replace('sqrt', 'math.sqrt')
    return equation


def solve(eq, value):
    neweq = eq.replace('x', str(value))
    return eval(neweq)


def bisection():
    a = (input("Enter interval a: "))
    b = (input("Enter interval b: "))
    if((solve(eq, a) * solve(eq, b)) > 0):
        q = raw_input("May not be able to do bisection method, Proceed anyway? (y/n) -> ")
        if q == 'n':
            return
    errtol = (input("How many significant figures (Ex: 3 = .001): "))
    sig = float("0.{:0>{width}}".format("1", width=errtol))
    c = float((a + b) / 2)
    bcsub = (b - c)
    # padding = ":"+str(len(str(errtol)))+"s"
    print "{:^5s}   {:^25}   {:^25}   {:^25}   {:^25}".format("n", "a", "b", "c", "b-c")
    print "{:-^120}".format("-")
    count = 0
    while bcsub > sig:
        count = count + 1
        print('{:^5s} | {:^25s} | {:^25s} | {:^25s} | {:^25s}'.format(str(count), str(a), str(b), str(c), str(bcsub)))
        if (solve(eq, b) * solve(eq, c)) < 0:
            a = c
        else:
            b = c
        c = float((a + b) / 2)
        bcsub = (b - c)
    count = count + 1
    print('{:^5s} | {:^25s} | {:^25s} | {:^25s} | {:^25s}'.format(str(count), str(a), str(b), str(c), str(bcsub)))
    print "{:-^120}".format("-")
    print('\nThe root is %s at interval [%s, %s]' % (str(c), str(a), str(b)))


def secant():
    x0 = (input("Enter an x0: "))
    x1 = (input("Enter an x1: "))
    errtol = (input("How many significant figures (Ex: 3 = .001):  "))
    sig = float("0.{:0>{width}}".format("9", width=errtol))
    print "{:^5s}   {:^25}   {:^25}".format("n","x0", "f(x)")
    print "{:-^65}".format("-")
    count = 0
    while True:
        count = count + 1
        fx = solve(eq, x1)
        result = (x1 - (solve(eq,x1) * ((x1 - x0)/(solve(eq,x1)-solve(eq, x0)))))
        x0 = x1
        x1 = result
        print('{:^5s} | {:^25s} | {:^25s}'.format(str(count), str(x0), str(fx)))
        if abs(fx) <= sig:
            break
    print "{:-^65}".format("-")
    print("\nThe root is: " + str(x0))


def newton():
    deq = parseEq(raw_input("Enter derivative of the function\n"))
    x0 = (input("Enter x0\n"))
    errtol = (input("How many significant figures (Ex: 3 = .001): "))
    sig = float("0.{:0>{width}}".format("9", width=errtol))
    #print sig
    print "{:^5s}   {:^25}   {:^25}   {:^25}   {:^25}".format("n", "x0", "f(x)", "f\'(x)", "x0 - (f(x)/f\'(x))")
    print "{:-^116}".format("-")
    count = 0
    while True:
        count = count + 1
        r = solve(eq, x0)
        dr = solve(deq, x0)
        result = (x0 - (r/dr))
        temp = x0
        x0 = result
        #print(abs(x0 - temp))
        print('{:^5s} | {:^25s} | {:^25s} | {:^25s} | {:^25s}'.format(str(count), str(temp), str(r), str(dr), str(result)))
        if abs(x0 - temp) <= sig:
            count = count + 1
            print('{:^5s} | {:^25s} | {:^25s} | {:^25s} | {:^25s}'.format(str(count), str(x0), str(r), str(dr), str(result)))
            break
    print "{:-^116}".format("-")
    print '\nThe root is: ' + str(x0)


cont = 'y'
while cont == 'y':
    eq = parseEq(raw_input("Enter function\n"))
    choice = input("1: Bisection\n2: Secant\n3: Newton\n4: QUIT\nWhich method to use? -> ")
    if choice == 1:
        bisection()
    elif choice == 2:
        secant()
    elif choice == 3:
        newton()
    elif choice == 4:
        break
    else:
        print "Invalid input"
    cont = raw_input("Try another function? (y/n)\n")
print 'Exiting...'
