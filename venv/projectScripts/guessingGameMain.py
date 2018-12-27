from welcomeScreen import welcomeScreen
from guessingGame import guessingGame
import time
def main():
  startTime = time.time()
  print("Initialising Welcome Screen...\n")
  welcomeScreen()
  print("\nTime to guess!!\n")
  guess = input()
  guessingGame(guess)
  endTime = time.time()
  timePlayed = endTime - startTime
  print("Total time played: ", timePlayed)



