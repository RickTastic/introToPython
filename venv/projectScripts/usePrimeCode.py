import primeCode

def main():
    number = primeCode.getInput()
    if primeCode.isPrime(number):
        print(number, "is prime")
    else:
        print(number, "is NOT prime")

main()