import math

def getInput():
    '''
    This function prompts the user for a numeric input
    return: The user entered numeric input
    '''
    number = eval(input("Please enter an integer: "))
    return number

def isPrime(n):
    '''
    This function checks if an integer is a prime number
    author: Ashai Ramsunder
    param n: A non-negative integer
    return: True or False
    '''
    if n < 0 or not int(n):
        print(" Error: Please enter a positive integer")
    else:
        trialFactor = 2
        root = math.sqrt(n)
        while trialFactor <= root:
            if n % trialFactor == 0:
                return False
        return True
