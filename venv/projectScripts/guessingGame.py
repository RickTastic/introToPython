import random
import math

computerRandomNumber = 73
print("I have selected a random number between 0 and 100. Your job is to try and guess the number.")
print("I will provide you with tips of the number I have selected. To quit press q")
print("Please enter your first try: ")
guess = input()
while guess != "q":
  guess = int(guess)
  if guess == computerRandomNumber:
    print("Congradulations, you win!! The number selected is: ", computerRandomNumber)
    break;
  if computerRandomNumber > 50 and computerRandomNumber < 75:
    guess = input("Hint: Your number is between 51 and 74. Guess again!")
  if computerRandomNumber > 75:
    guess = input("Hint: Your number is greater than 75. Guess again!")
  if computerRandomNumber > 25 and computerRandomNumber < 50:
    guess = input("Hint: Your number is between 26 and 49. Guess again!")
  if computerRandomNumber < 25:
    guess = input("Hint: Your number is less than 25. Guess again!")
print("Exiting...")


