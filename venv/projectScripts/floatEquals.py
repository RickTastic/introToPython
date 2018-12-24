import math

# Equals (a, b, tolerance)
# This function checks if two numbers are equal up to a desired tolerance level.
# This is useful to cater for floating point rounding errors

def equals(a, b, tolerance):
    return a == b or math.fabs(a - b) < tolerance

def main():
    i = 0.0
    while not equals(i, 1.0, 0.0001):
        print("i =", i)
        i += 0.1

main()