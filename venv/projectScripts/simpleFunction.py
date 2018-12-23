# Prompt Function
def prompt():
  print("Please enter an integer value: ", end = "")

# Start the program and use the function defined above

print("This program sums two integers")
prompt()
value1 = int(input())
prompt()
value2 = int(input())
addition = value1 + value2
print(value1, "+", value2, "=", addition)