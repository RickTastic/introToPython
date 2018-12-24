# Global variable
result = 0.0
value1 = 0.0
value2 = 0.0

def help():
  print("Add: Adds two numbers")
  print("Subtract: Subtracts two numbers")
  print("Print: Displays the result of the latest operation")
  print("Help: Displays this help screen")
  print("Quit: Exits the program")

def menu():
  return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")

def getInput():
  global value1, value2
  value1 = float(input("Enter value 1: "))
  value2 = float(input("Enter value 2: "))

def report():
  print(result)

def add():
  global result
  result = value1 + value2

def subtract():
  global result
  result = value1 - value2

def main():
  done = False;
  while not done:
    choice = menu()
    if choice == 'A' or choice == 'a':
      getInput()
      add()
      report()
    elif choice == 'S' or choice == 's':
     getInput()
     subtract()
     report()
    elif choice == 'H' or choice == 'h':
      help()
    elif choice == 'P' or choice == 'p':
      report()
    else:
      done = True

main()