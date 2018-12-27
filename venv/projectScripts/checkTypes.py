import math
def checkTypes(guess):
  try:
    message = dict()
    if type(guess) == int:
      if guess < 0 or guess > 100:
        message['errorMessage'] = "Please enter an integer in the range 0...100."
        message['isValid'] = False
        return message
      else:
        message['errorMessage'] = ""
        message['isValid'] = True
        return message
    elif type(guess) == str and (guess == 'q' or guess == "Q"):
      message['errorMessage'] = ""
      message['isValid'] = True
      return message
    elif type(guess) == float:
      message['errorMessage'] = "The number " \
                                + str(guess) \
                                + " " \
                                + "is not valid. Did you mean " \
                                + str(math.floor(guess)) \
                                + " or " \
                                + str(math.ceil(guess)) \
                                + "?"
      message['isValid'] = False
      return message
    else:
      message['errorMessage'] = str(guess) + " is not a valid integer."
      message['isValid'] = False
      return message
  except Exception:
    raise Exception("Unknown Exception. Please restart the application")