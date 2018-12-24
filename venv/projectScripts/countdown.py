# This function demonstrates the concept of a default argument

def countdown(n = 10):
    for i in range(n, -1, -1):
        print(i)

# Use default argument
countdown()

# Use defined argument
countdown(n = 15)