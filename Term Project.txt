# Term Project: Build a number guessing game. The player must guess the answer that lies between 0 and 100. To start, the answer is 27.


# Week 1 Start
# Question: How many variables do you think you need?
# Hint: Re-read the question to see how many boundaries and other numbers need to exist.
# Write your variable(s) in the format {variable name} = {value}


# Week 1 Answer
lowerBoundary = 0
upperBoundary = 100
answer = 27


# Week 2 Start
# Question: How do you solicit user input?
# Hint: Google user input in python


# Question: How do you check if the number guessed is above or below the answer? How do you indicate the user guessed the correct number?
# Hint: Google if statements in python


# Week 2 Answer
userGuess = input("Please enter your guess: ")
print("The user guessed: " + userGuess)


# VERY IMPORTANT: You need to convert userGuess to an int so the types match. You can't compare a string and an int. You can only compare variables that are the same type.
if int(userGuess) > answer:
  print("Your guess is too high")


if int(userGuess) < answer:
  print("Your guess is too low")


if int(userGuess) == answer:
  print("You win!")




# Week 3 Start
# Question: What is the biggest problem with the code so far? How many attempts does a user have? How can we allow a user to have more guesses?
# Hint: Use a while loop. What is the benefit of a while loop? What condition would the loop need? Remember about data type conversion!


# Week 3 Answer
while (int(userGuess) != answer):
  print("While....")
  userGuess = input("Please enter your guess: ")
  print("The user guessed: " + userGuess)
  
  if int(userGuess) > answer:
    print("Your guess is too high")


  if int(userGuess) < answer:
    print("Your guess is too low")


  if int(userGuess) == answer:
    print("You win!")




# Week 4 Start
# Question: How would we generate a random number between the lower and upper boundaries? Will you need to import a library?
    
# Question: How could we re-factor our code to use functions?
# Task: Print the randomly generated answer to the screen to check your answer is correct


# Week 4 Answer
import random
answer = random.randint(lowerBoundary, upperBoundary)
print("randomly generated answer: " + str(answer))