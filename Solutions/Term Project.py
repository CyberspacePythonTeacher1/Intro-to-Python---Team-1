import random

# Term Project: Build a number guessing game. The player must guess the answer that lies between 0 and 100. 
def checkAnswer(userGuess):
  print("The user guessed: ", userGuessInteger)

  if userGuessInteger > answer:
    print("Your guess is too high")

  if userGuessInteger < answer:
    print("Your guess is too low")

  if userGuessInteger == answer:
    print("You win!")  

def getUserInputInteger():
  # Week 2 Start
  # Question: How do you solicit user input?
  # Hint: Google user input integer in python
  # VERY IMPORTANT: You need to convert userGuess to an int so the types match. You can't compare a string and an int. You can only compare variables that are the same type.

  userGuess = input("Please enter your guess: ")
  userGuessInteger = int(userGuess)
  return userGuessInteger



# Week 1 Answer
lowerBoundary = 0
upperBoundary = 100

# Week 4 Start
# Question: How would we generate a random number between the lower and upper boundaries? Will you need to import a library?
    
# Question: How could we re-factor our code to use functions?
# Task: Print the randomly generated answer to the screen to check your answer is correct
answer = random.randint(lowerBoundary, upperBoundary)
print("randomly generated answer: ", answer)

userGuessInteger = 0

# Week 3 Start
# Question: What is the biggest problem with the code so far? How many attempts does a user have? How can we allow a user to have more guesses?
# Hint: Use a while loop. What is the benefit of a while loop? What condition would the loop need? Remember about data type conversion!

# Week 3 Answer
while (userGuessInteger != answer):
  print("While....")
  userGuessInteger = getUserInputInteger()
  checkAnswer(userGuessInteger)
