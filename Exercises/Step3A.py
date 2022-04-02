# Term Project: Build a number guessing game. The player must guess the answer that lies between 0 and 100. 
# To start, the number is the answer to life the universe and everything, 42

# Week 1 Start
# Question: How many variables do you think you need?
# Hint: Re-read the question to see how many boundaries and other numbers need to exist.
# Write your variable(s) in the format {variable name} = {value}

# Week 1 Answer
lowerBoundary = 0
upperBoundary = 100
answer = 42
print("The answer to life, the universe and everything else is ", answer)

# Week 2 Start
# Question: How do you solicit user input?
# Hint: Google user input integer in python
# VERY IMPORTANT: You need to convert userGuess to an int so the types match. You can't compare a string and an int. You can only compare variables that are the same type.

userGuess = input("Please enter your guess: ")
userGuessInteger = int(userGuess)
print("The user guessed: " + userGuess)

# Question: How do you check if the number guessed is above or below the answer? How do you indicate the user guessed the correct number?
# Hint: Google if statements in python

# Week 2 Answer
if userGuessInteger > answer:
  print("Your guess is too high")

if userGuessInteger < answer:
  print("Your guess is too low")

if userGuessInteger == answer:
  print("You win!")

# Week 3 Start
# Question: What is the biggest problem with the code so far? How many attempts does a user have? How can we allow a user to have more guesses?
# Hint: Use a while loop. What is the benefit of a while loop? What condition would the loop need? Remember about data type conversion!