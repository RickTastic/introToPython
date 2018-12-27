import random
import checkTypes
def guessingGame():
  """
  This is the logic for the guessing game. Advanced hints and features to be added.
  author: Ashai Ramsunder
  param guess: An integer guess
  return:
  """
  guess = input()
  done = False
  while not done:
    computerRandomNumber = 44
    typeCheck = checkTypes.checkTypes(guess)
    countGuess = 1
    if typeCheck['isValid']:
      if guess == computerRandomNumber:
        print("Congratulation's, you win!! My random number is: ", computerRandomNumber)
        print("The number of tries taken to guess my number is: ", countGuess)
        tryAgain = input("Would you like to try again? (y/n)")
        if tryAgain == 'n':
          done = True
        else:
          computerRandomNumber = 85
          print("I have selected a new number between 0 and 100, try and guess the number or press q to quit!")
          countGuess = 1
          guess = input()
      if guess == 'q':
        done = True
      if computerRandomNumber > 50 and computerRandomNumber < 75:
        guess = input("Hint: Your number is between 51 and 74. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber > 75:
        guess = input("Hint: Your number is greater than 75. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber > 25 and computerRandomNumber < 50:
        guess = input("Hint: Your number is between 26 and 49. Guess again!\n")
        countGuess += 1
        print()
      if computerRandomNumber < 25:
        guess = input("Hint: Your number is less than 25. Guess again!\n")
        countGuess += 1
        print()
    else:
      print(typeCheck['errorMessage'])
      done = False
  print("Exiting...")