def help():
  print("Add: Adds two numbers")
  print("Subtract: Subtracts two numbers")
  print("Print: Displays the result of the latest operation")
  print("Help: Displays this help screen")
  print("Quit: Exits the program")

def menu():
  return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")

def main():
  result = 0.0
  done = False;
  while not done:
    choice = menu()
    if choice == 'A' or choice == 'a':
      value1 = float(input("Enter value 1: "))
      value2 = float(input("Enter value 2: "))
      result = value1 + value2
      print(result)
    elif choice == 'S' or choice == 's':
      value1 = float(input("Enter value 1: "))
      value2 = float(input("Enter value 2: "))
      result = value1 - value2
      print(result)
    elif choice == 'H' or choice == 'h':
      help()
    elif choice == 'P' or choice == 'p':
      print(result)
    else:
      done = True