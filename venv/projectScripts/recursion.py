# This function illustrates the concept of recursion by computing the factorial of an integer n

def recursion(n):
    if n == 0:
        return 1
    else:
        return n * recursion(n - 1)

def main():
    print(" 0! = ", recursion(0))
    print(" 1! = ", recursion(1))
    print(" 6! = ", recursion(6))
    print(" 23! = ", recursion(23))

main()