import math
print "{:^5}   {:^10}   {:^20}   {:^20}   {:^20}".format("n", "n!", "Stirling Approx", "Absolute Error", "Relative error")
print "{:-^90}".format("-")
for n in range(1, 11):
    fac = (math.factorial(n))
    Sapprox = float(math.sqrt(2*math.pi*n)*(math.pow((n/math.e), n)))
    Aberror = float(fac - Sapprox)
    Relerror = float(Aberror/fac)
    print("{:^5} | {:^10} | {:^20.11f} | {:^20.11f} | {:^20.11f}".format(n, fac, Sapprox, Aberror,  Relerror))
print "{:-^90}".format("-")
    # Absolute error grows with n!
    # Relative error shrinks with n!
