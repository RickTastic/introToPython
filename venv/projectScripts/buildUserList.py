# Builds a custom list of non-negative integers defined by the user

def buildUserList():
  """
  Builds a list from input provided by the user
  :return: A list of non-negative integers
  """
  userList = []
  done = False
  while not done:
    listEnteries = eval(input("Please enter a non-negative integer to add to the list, hit -1 to escape"))
    if listEnteries == -1:
      done = True
    else:
      userList += [listEnteries]
  return userList

def main():
  inputList = buildUserList()
  print(inputList)

if __name__ == "__main__":
  main()