#! /usr/bin/env python3

# Darren Butler
# Calculate the square root of a number

def sqrt(x):
    """
    Calculate the square root of argument x
    """
    
    # check that x is positive
    if x < 0:
        print("error, negative value supplied")
        return -1 



    # initial quguess for the square root
    z = x / 2.0

    # continuously improve the guess
    while abs(x - (z*z)) > 0.000001:
        z -= (z*z - x) / (2*z)

    return z

myval = 63.0
print("The square root of", myval, "is", sqrt(myval))
