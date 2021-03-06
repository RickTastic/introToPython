# This module contains a gcd function that computes the gcd of two integers
# This module also contains the prompt function to get the integers along with a main method
def gcd(m, n):
   min = m if m < n else n
   largestFactor = 1
   for i in range(1, min + 1):
     if m % i == 0 and n % i == 0:
       largestFactor = i
   return largestFactor

def getIntegers():
  return int(input("Please enter an integer: "))

def main():
  n = getIntegers()
  m = getIntegers()
  print("gcd(", n, ",", m, ") = ", gcd(m, n), sep = "")