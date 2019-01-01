a = [10, 20, 30, 40]
b = [10, 20, 30, 40]

print("Is", a, " equal to ", b, "?", sep = '', end = ' ')
print(a == b)

print("Are", a, " and ", b, "aliases?", sep = '', end = ' ')
print(a is b)

c = [100, 200, 300, 400]
d = c

print("Is", c, " equal to ", d, "?", sep = '', end = ' ')
print(c == d)

print("Are", c, " and ", d, "aliases?", sep = '', end = ' ')
print(c is d)