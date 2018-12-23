import time

print("Enter your name: ", end = "")
startTime = time.perf_counter()
name = input()
elapsed = time.perf_counter() - startTime
print(name, "it took you", elapsed, "seconds to respond")