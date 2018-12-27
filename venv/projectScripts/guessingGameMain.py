# This script is a basic guessing game
import random
from welcomeScreen import welcomeScreen
computerRandomNumber = random.randrange(0, 100)
welcomeScreen()
guess = input()
countGuess = 1
done = False
while not done:
  guess = int(guess)
  if int(guess) < 0:
    print("The number", guess, "is less than zero. Please enter a number between 0 and 100.")
    guess = input()
  if int(guess) > 100:
    print("The number", guess, "is greater than 100. Please enter a number between 0 and 100")
    guess = input()
  if guess == computerRandomNumber:
    print("Congratulation's, you win!! My random number is: ", computerRandomNumber)
    print("The number of tries taken to guess my number is: ", countGuess)
    tryAgain = input("Would you like to try again? (y/n)")
    if tryAgain == 'n':
      done = True
    else:
      computerRandomNumber = random.randrange(0, 100)
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
print("Exiting...")


